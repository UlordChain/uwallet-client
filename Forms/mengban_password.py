# -*- coding: utf-8 -*-
# @Time    : 2017/12/18
# @Author  : Shu
# @Email   : httpservlet@yeah.net

from PyQt4.QtCore import *
from PyQt4.QtGui import *
from FormUI.ui_update_password import Ui_updatepasswordWD


class PasswordWidget(QWidget, Ui_updatepasswordWD):
    def __init__(self, parent=None):
        super(PasswordWidget, self).__init__(parent)
        self.setupUi(self)
        self.parent = parent
        self.password = ''
        self.setStyleSheet("""QFrame#frame_left{border-image:url(:/images/heisemengban)}
                                QFrame#frame_top{border-image:url(:/images/baisemengban)}
                                QFrame#frame_rigth{background-color:white;}
                                """)
        self.btn_password_close.clicked.connect(self.close)
        self.btn_passwod_ok.clicked.connect(self.slot_ok)
        self.led_password_current.textChanged.connect(self.slot_current_edit)
        self.led_password_new.textChanged.connect(self.slot_password_edit)
        self.led_password_comfirm.textChanged.connect(self.slot_password_edit)
        self.frame_left.installEventFilter(self.parent)
        self.frame_top.installEventFilter(self.parent)

    def slot_ok(self):
        try:
            args = ['password', '--client', '--guinewpassword', self.password, ]
            if self.lbl_password_current.isVisible() and self.led_password_current.isVisible():
                if self.led_password_current.text().isEmpty():
                    self.led_password_current.setStyleSheet("""border:1px solid red;""")
                    return

                args.append('-W')
                current_password = unicode(self.led_password_current.text()).encode('utf-8')
                args.append(current_password)
            rs = self.parent.bwallet_main(*args, thread_safe=True)
        except Exception as e:
            print (e)
            if 'Incorrect password' in str(e):
                self.led_password_current.setStyleSheet("""border:1px solid red;""")
            else:
                self.led_password_current.setStyleSheet("""border:1px solid yellow;""")
        else:
            self.close()

    def slot_password_edit(self, text):
        if self.led_password_new.text() == self.led_password_comfirm.text():
            self.password = unicode(self.led_password_new.text()).encode('utf-8')
            self.btn_passwod_ok.setEnabled(True)
            self.led_password_new.setStyleSheet('')
            self.led_password_comfirm.setStyleSheet('')
        else:
            self.btn_passwod_ok.setEnabled(False)
            self.led_password_new.setStyleSheet('border:1px solid red;')
            self.led_password_comfirm.setStyleSheet('border:1px solid red;')

        if self.led_password_current.isVisible() and self.led_password_current.text().isEmpty():
            self.btn_passwod_ok.setEnabled(False)

    def slot_current_edit(self):
        self.led_password_current.setStyleSheet("")
