# -*- coding: utf-8 -*-
# @Time    : 2017/12/16
# @Author  : Shu
# @Email   : httpservlet@yeah.net

from PyQt4.QtGui import *
from PyQt4.Qt import *
from PyQt4.QtCore import *


class BaseMenu(QMenu):
    def __init__(self, parent=None):
        super(BaseMenu, self).__init__(parent)

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
        self.addAction(action)


class FileMenu(BaseMenu):
    def __init__(self, parent=None):
        super(FileMenu, self).__init__(parent)

        self.createAction(self.tr('&Open'), slot=self.openfile,checkable=True)
        self.addSeparator()
        self.createAction(self.tr('&Quit'), slot=self.openfile)

    def openfile(self):
        print 'openfile'


class WalletMenu(BaseMenu):
    def __init__(self, parent=None):
        super(WalletMenu, self).__init__(parent)

        self.createAction(self.tr('&Infomation'), slot=self.openfile)

    def openfile(self):
        print 'openfile'


class ViewMenu(BaseMenu):
    def __init__(self, parent=None):
        super(ViewMenu, self).__init__(parent)

        self.createAction(self.tr('&Show'), slot=self.openfile)

    def openfile(self):
        print 'openfile'


class ToolsMenu(BaseMenu):
    def __init__(self, parent=None):
        super(ToolsMenu, self).__init__(parent)

        self.createAction(self.tr('&Preferences'), slot=self.openfile)

    def openfile(self):
        print 'openfile'


class HelpMenu(BaseMenu):
    def __init__(self, parent=None):
        super(HelpMenu, self).__init__(parent)

        self.createAction(self.tr('&About'), slot=self.openfile)

    def openfile(self):
        print 'openfile'
