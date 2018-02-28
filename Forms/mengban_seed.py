# -*- coding: utf-8 -*-
# @Time    : 2017/12/18
# @Author  : Shu
# @Email   : httpservlet@yeah.net

from PyQt4.QtCore import *
from PyQt4.QtGui import *
from FormUI.ui_getseed import Ui_getseedWD


class SeedWidget(QWidget, Ui_getseedWD):
    def __init__(self, parent=None):
        super(SeedWidget, self).__init__(parent)
        self.setupUi(self)
        self.parent = parent
        self.setStyleSheet("""QFrame#frame_left{border-image:url(:/images/heisemengban)}
                                QFrame#frame_top{border-image:url(:/images/baisemengban)}
                                QFrame#frame_rigth{background-color:white;}
                                """)
        self.ted_setting_getseed.setReadOnly(True)
        self.btn_seed_password.clicked.connect(self.slot_password)
        self.frame_left.installEventFilter(self.parent)
        self.frame_top.installEventFilter(self.parent)

    def slot_password(self):
        """查看seed之前, 需要输入密码"""
        if self.led_seed_password.text().isEmpty():
            self.led_seed_password.setStyleSheet("""border:1px solid red;""")
        else:
            self.led_seed_password.setStyleSheet("")
            password = unicode(self.led_seed_password.text()).encode('utf-8')
            try:
                args = ['getseed', '--client']
                if password:
                    args.append('-W')
                    args.append(password)
                rs = self.parent.bwallet_main(*args, thread_safe=True)
            except Exception as e:
                print (e)
                if 'Incorrect password' in str(e):
                    self.led_seed_password.setStyleSheet("""border:1px solid red;""")
                else:
                    self.led_seed_password.setStyleSheet("""border:1px solid yellow;""")
            else:
                self.ted_setting_getseed.setText(rs)
                self.ted_setting_getseed.setVisible(True)
                self.led_seed_password.setVisible(False)
                self.btn_seed_password.setVisible(False)

