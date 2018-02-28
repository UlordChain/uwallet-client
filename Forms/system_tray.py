# -*- coding: utf-8 -*-
# @Author       : Shu
# @Email        : httpservlet@yeah.net
# @Date         : 2017/12/20
# @Description  :

from PyQt4.QtGui import *
import qtawesome as qta


class MySystemTrayIcon(QSystemTrayIcon):
    """ 系统托盘图标类 """

    def __init__(self, parnet):
        super(MySystemTrayIcon, self).__init__(parnet)
        self.parent = parnet
        self.create_context_menu()

    def create_context_menu(self):
        """ 创建系统托盘的菜单 """
        self.menu = QMenu()

        self.normal = QAction(self.menu)
        self.normal.setIcon(qta.icon('ei.screen', color='#b1b1b1'))
        self.normal.triggered.connect(self.parent.show)

        self.exit_ = QAction(self.menu)
        self.exit_.setIcon(qta.icon('ei.off', color='#b1b1b1'))
        self.exit_.triggered.connect(self.parent.close)

        self.menu.addAction(self.normal)
        self.menu.addSeparator()
        self.menu.addAction(self.exit_)
        self.setContextMenu(self.menu)

        self.retranslateUi()

    def retranslateUi(self):
        """自定义动态翻译文本的方法(模仿UI生成文件)"""
        self.normal.setText(self.tr("&View UWallet"))
        self.exit_.setText(self.tr("&Exit UWallet"))

