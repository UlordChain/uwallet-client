# -*- coding: utf-8 -*-
# @Time    : 2017/12/14
# @Author  : Shu
# @Email   : httpservlet@yeah.net

import base64
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from FormUI.ui_content import Ui_contentWD
from Forms.qrcode_widget import QRCodeWidget


class ContentWidget(QWidget, Ui_contentWD):
    def __init__(self, parent=None):
        super(ContentWidget, self).__init__(parent)
        self.setupUi(self)
        self.parent = parent

        self.tip_text = ''
        # 先去掉描述文本框和label
        self.lbl_password.setVisible(False)
        self.led_send_password.setVisible(False)
        self.btn_preview.setVisible(False)
        self.lbl_result.setVisible(False)
        self.btn_max_amount.setVisible(False)

        self.twd_history.setColumnWidth(0, 150)
        self.twd_history.setColumnWidth(1, 150)
        self.twd_history.setColumnWidth(2, 150)

        self.twd_addresses.setColumnWidth(0, 320)
        self.twd_addresses.setColumnWidth(1, 150)
        self.twd_addresses.setColumnWidth(2, 150)
        self.twd_addresses.setColumnWidth(3, 150)

        re = QRegExp("^\d+(\.\d{1,6})?$")
        self.led_send_amount.setValidator(QRegExpValidator(re, self))
        self.btn_clear.clicked.connect(self.slot_clear)
        self.btn_send.clicked.connect(self.slot_send)

        self.twd_addresses.setContextMenuPolicy(Qt.CustomContextMenu)
        self.twd_addresses.customContextMenuRequested.connect(self.show_menu)

        self.cmb_receiving_change.currentIndexChanged.connect(self.slot_receiving_textchange)
        self.cmb_all.currentIndexChanged.connect(self.slot_all)
        self.led_receiving_address.textChanged.connect(self.slot_receive_textchange)

        self.qrw = QRCodeWidget(fixedSize=220, parent=self)
        # self.horizontalLayout_receive.addWidget(self.qrw)
        self.horizontalLayout_receive.insertWidget(2, self.qrw)
        QTimer.singleShot(0, self.init_menu)

    def slot_clear(self):
        self.led_send_payto.clear()
        self.led_send_amount.clear()

        self.lbl_password.setVisible(False)
        self.led_send_password.setVisible(False)
        self.lbl_result.setVisible(False)

    def slot_send(self):
        self.lbl_result.setVisible(False)
        self.repaint()
        status = self.parent.bwallet_main('daemonisrunning', '--client')
        if status is not True:
            self.lbl_result.setVisible(True)
            self.lbl_result.setText(self.tr('Daemon is not running'))
            self.tip_text = 'Daemon is not running'
            self.lbl_result.setStyleSheet("""border:1px solid rgba(75, 164, 156,30%);
background-color:rgba(104,202,193,30%);color:rgba(255,0,0,60%);""")
            return

        try:
            self.btn_send.setEnabled(False)
            self.repaint()

            empty = False
            payto = self.led_send_payto.text()
            amount = self.led_send_amount.text()
            if payto.isEmpty():
                empty = True
                self.led_send_payto.setStyleSheet("""border-color:#FF6666;""")
            else:
                self.led_send_payto.setStyleSheet("")
                payto = unicode(payto).encode('utf-8')

            if amount.isEmpty():
                empty = True
                self.led_send_amount.setStyleSheet("""border-color:#FF6666;""")
            else:
                self.led_send_amount.setStyleSheet("")
                amount = unicode(amount).encode('utf-8')

            if empty is True:
                return

            args = ['paytoandsend', payto, amount]
            haspassword = self.parent.bwallet_main('haspassword', '--client')
            if haspassword is True:
                if self.led_send_password.isVisible():

                    password = self.led_send_password.text()
                    if not password.isEmpty():
                        self.led_send_password.setStyleSheet("")
                        password = unicode(password).encode('utf-8')
                        args.append('-W')
                        args.append(password)
                    else:
                        self.led_send_password.setStyleSheet("""border-color:#FF6666;""")
                        return
                else:
                    self.lbl_password.setVisible(True)
                    self.led_send_password.setVisible(True)
                    self.led_send_password.setStyleSheet("""border-color:#FF6666;""")
                    return

            args.append('--client')
            try:
                # 发送成功, 返回交易ID
                if self.parent.command_walker.isRunning():
                    self.parent.command_walker.stop()
                    self.parent.command_walker.wait()
                # 在做支付操作的时候, 先停止线程中执行的钱包命令
                # 因为不知道什么原因, 一个进程中, 如果两个线程同时执行钱包命令
                # 会导致返回结果错乱, 所以在执行支付操作时, 先停止其他命令的执行
                txid = self.parent.bwallet_main(*args)
                self.parent.command_walker.start()
            except Exception as e:
                self.lbl_result.setVisible(True)
                if 'Invalid Bitcoin address or alias' in str(e):
                    self.lbl_result.setText(self.tr('Address wrong'))
                    self.tip_text = 'Address wrong'
                elif 'expected string or buffer' in str(e):
                    self.lbl_result.setText(self.tr('Address wrong'))
                    self.tip_text = 'Address wrong'
                elif 'NotEnoughFunds' in str(e):
                    self.lbl_result.setText(self.tr('Not enough funds'))
                    self.tip_text = 'Not enough funds'
                else:
                    self.lbl_result.setText(self.tr('Pay for failure!'))
                    self.tip_text = 'Pay for failure!'

                self.lbl_result.setStyleSheet("""border:1px solid rgba(75, 164, 156,30%);
                                background-color:rgba(104,202,193,30%);color:rgba(255,0,0,60%);""")
            else:
                self.lbl_result.setVisible(True)
                tx_status = False
                try:
                    base64.b64decode(txid)
                    tx_status = True
                except:
                    pass

                if tx_status and len(txid) == 64:
                    self.lbl_result.setText(self.tr('Pay for success!'))
                    self.tip_text = 'Pay for success!'
                    self.lbl_result.setStyleSheet("""border:1px solid rgba(75, 164, 156,30%);
                    background-color:rgba(104,202,193,30%);color:rgba(0,128,0,60%);""")
                else:
                    self.lbl_result.setText(self.tr('Pay for failure!'))
                    self.tip_text = 'Pay for failure!'
                    self.lbl_result.setStyleSheet("""border:1px solid rgba(75, 164, 156,30%);
                    background-color:rgba(104,202,193,30%);color:rgba(255,0,0,60%);""")
        finally:
            self.btn_send.setEnabled(True)

    def slot_receiving_textchange(self, index):
        filter_1 = None
        if index == 0:
            filter_1 = '--receiving'
        elif index == 1:
            filter_1 = '--change'
        self.parent.command_walker.set_args(filter_1=filter_1)
        self.reboot_command_walker()

    def slot_all(self, index):
        filter_2 = None
        if index == 0:
            filter_2 = 'all'
        elif index == 1:
            filter_2 = '--unused'
        elif index == 2:
            filter_2 = '--funded'
        elif index == 3:
            filter_2 = '--frozen'
        self.parent.command_walker.set_args(filter_2=filter_2)
        self.reboot_command_walker()

    def reboot_command_walker(self):
        if self.parent.command_walker.isRunning():
            self.parent.command_walker.stop()
            self.parent.command_walker.wait()
            self.parent.command_walker.start()

    def init_menu(self):
        self.context_menu = QMenu(self.twd_addresses)
        self.action_copy = self.createAction(self.tr('Copy Address'), self.copy_address)
        self.action_pay = self.createAction(self.tr('Request Payment'), self.request_payment)
        self.context_menu.addAction(self.action_copy)
        self.context_menu.addAction(self.action_pay)

    def show_menu(self):
        self.context_menu.exec_(QCursor().pos())

    def slot_receive_textchange(self, text):
        self.qrw.setData(unicode(text))

    def createAction(self, text, slot=None, shortcut=None, icon=None, tip=None, checkable=False, signal="triggered()"):
        """ triggered,当调用QAction时,发射信号
        toggled:开关某个复选动作,发送信号; 手动点击或者调用setChecked(),发送信号
        triggered:触发某个动作,发送信号; 手动点击或者调用trigger(),发送信号; setChecked()或toggle() 不能发送
        """
        action = QAction(text, self)  # 设置父对象self,表明该动作在此父对象及以下窗体中可用
        if icon is not None:
            action.setIcon(QIcon(":/%s.png" % icon))  # 菜单图标,:/会告诉pyqt,这是一个资源
        if shortcut is not None:
            action.setShortcut(shortcut)  # 快捷键,可以直接设置字符串,如 "Ctrl+M"
        if tip is not None:
            action.setToolTip(tip)  # 悬浮提示
            action.setStatusTip(tip)  # 状态栏提示
        if slot is not None:
            self.connect(action, SIGNAL(signal), slot)
        if checkable:
            action.setCheckable(True)  # 设置为复选动作(就是变成可以选中和不选中两个状态)
        return action

    def copy_address(self):
        address = unicode(self.twd_addresses.selectedItems()[0].text(0))
        board = QApplication.clipboard()
        board.setText(address)

    def request_payment(self):
        address = unicode(self.twd_addresses.selectedItems()[0].text(0))
        self.led_receiving_address.setText(address)
        self.stackedWidget.setCurrentIndex(3)
        # 发送按钮的clicked信号, 改变顶部导航的选中状态
        self.parent.title_widget.tbt_receive.click()

    def custom_retranslateUi(self):
        self.action_copy.setText(self.tr('Copy Address'))
        self.action_pay.setText(self.tr('Request Payment'))
        self.lbl_result.setText(self.tr(self.tip_text))
