# -*- coding: utf-8 -*-
# @Author       : Shu
# @Email        : httpservlet@yeah.net
# @Date         : 2017/12/25
# @Description  :


import traceback
import time
from PyQt4.QtGui import *
from PyQt4.QtCore import *


class CommandsWalker(QThread):
    def __init__(self, filter_1=None, filter_2=None, interval=5, parent=None):
        super(CommandsWalker, self).__init__(parent)
        self.parent = parent
        self.filter_1 = filter_1
        self.filter_2 = filter_2
        self.interval = interval  # 更新间隔(单位:秒)
        self.stopped = False
        self.mutex = QMutex()

    def set_args(self, filter_1=None, filter_2=None):
        if filter_1:
            self.filter_1 = filter_1
        if filter_2:
            if filter_2 == 'all':
                self.filter_2 = None
            else:
                self.filter_2 = filter_2

    def initialize(self):
        with QMutexLocker(self.mutex):
            self.stopped = False

    def stop(self):
        with QMutexLocker(self.mutex):
            self.stopped = True

    def isStopped(self):
        with QMutexLocker(self.mutex):
            return self.stopped

    def run(self):
        self.initialize()
        time.sleep(1)
        while True:
            try:
                # 本来这是三个线程独立去执行不同的命令,
                # 但是多线程同时去执行命令会互相干扰,
                # 比如用listaddresses可能返回的是另外一个线程history的结果
                # 所以这里串行化执行三个命令 daemon start, history, listaddresses
                rs = self.run_daemon()
                if rs == 'stop':
                    return
                rs = self.run_balance()
                if rs == 'stop':
                    return
                rs = self.run_address()
                if rs == 'stop':
                    return
                rs = self.run_history()
                if rs == 'stop':
                    return
            except:
                print traceback.format_exc()
                self.sleep(self.interval)
            else:
                self.sleep(self.interval)

    def sleep(self, sec=30):
        for i in range(int(10 * sec)):
            if self.isStopped():
                return
            time.sleep(0.1)

    def run_history(self):
        if self.isStopped():
            return 'stop'
        args = ['history', '--client']
        historys = self.parent.bwallet_main(*args)
        items = self.parent.content_widget.twd_history.selectedItems()
        if self.isStopped():
            return 'stop'
        txid = None
        if len(items) >= 1:
            txid = unicode(items[0].data(0, Qt.UserRole).toString())
        if self.isStopped():
            return 'stop'
        if isinstance(historys, list):
            # 有时候返回的是bool值
            self.emit(SIGNAL("history"), historys, txid)
        if self.isStopped():
            return 'stop'

    def run_address(self):
        if self.isStopped():
            return 'stop'
        args = ['listaddresses', '-b', '--client']
        if self.filter_1:
            args.append(self.filter_1)
        if self.filter_2:
            args.append(self.filter_2)
        listaddresses = self.parent.bwallet_main(*args)
        items = self.parent.content_widget.twd_addresses.selectedItems()
        if self.isStopped():
            return 'stop'
        cur_addr = None
        if len(items) >= 1:
            cur_addr = unicode(items[0].data(0, Qt.UserRole).toString())
        if self.isStopped():
            return 'stop'
        if isinstance(listaddresses, list):
            # 有时候返回的是bool值
            self.emit(SIGNAL("address"), listaddresses, cur_addr)
        if self.isStopped():
            return 'stop'

    def run_daemon(self):
        if self.isStopped():
            return 'stop'
        status = self.parent.bwallet_main('daemonisrunning', '--client')
        if self.isStopped():
            return 'stop'
        self.emit(SIGNAL("daemon"), status)
        if self.isStopped():
            return 'stop'

    def run_balance(self):
        if self.isStopped():
            return 'stop'
        balance = self.parent.bwallet_main('getbalance', '--client')
        if self.isStopped():
            return 'stop'
        if isinstance(balance, dict):
            balance = balance.get('confirmed', 0)
            if balance:
                self.emit(SIGNAL("balance"), str(balance))
        if self.isStopped():
            return 'stop'
