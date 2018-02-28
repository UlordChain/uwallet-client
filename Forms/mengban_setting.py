# -*- coding: utf-8 -*-
# @Time    : 2017/12/18
# @Author  : Shu
# @Email   : httpservlet@yeah.net

from PyQt4.QtCore import *
from PyQt4.QtGui import *
from FormUI.ui_setting import Ui_settingWD


class SettingtWidget(QWidget, Ui_settingWD):
    def __init__(self, parent=None):
        super(SettingtWidget, self).__init__(parent)
        self.setupUi(self)
        self.parent = parent
        self.setStyleSheet("""QFrame#frame_left{border-image:url(:/images/heisemengban)}
                                QFrame#frame_top{border-image:url(:/images/baisemengban)}
                                QFrame#frame_rigth{background-color:white;}
                                """)
        self.frame_left.installEventFilter(self.parent)
        self.frame_top.installEventFilter(self.parent)
