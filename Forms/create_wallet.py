# -*- coding: utf-8 -*-
# @Author       : Shu
# @Email        : httpservlet@yeah.net
# @Date         : 2017/12/22
# @Description  :

from PyQt4.QtCore import *
from PyQt4.QtGui import *
from FormUI.ui_create_wallet import Ui_CreateWallet


class CreateWalletDialog(QDialog, Ui_CreateWallet):
    def __init__(self, parent=None):
        super(CreateWalletDialog, self).__init__(parent)
        self.parent = parent
        self.setupUi(self)
        self.setAttribute(Qt.WA_DeleteOnClose, True)
        # self.setWindowFlags(Qt.FramelessWindowHint)  # 设置无边框
        self.password = ''

        icon_pixmap = QPixmap(':/images/ico')
        # icon_pixmap=icon_pixmap.scaled(self.lbl_icon.size(), Qt.KeepAspectRatio)
        self.lbl_icon.setPixmap(icon_pixmap)
        self.led_password.textChanged.connect(self.slot_password_edit)
        self.led_confirm_password.textChanged.connect(self.slot_password_edit)
        self.btn_cancel.clicked.connect(parent.close)
        self.btn_next.clicked.connect(self.slot_create_wallet)

    def slot_password_edit(self, text):
        if self.led_password.text() == self.led_confirm_password.text():
            self.password = unicode(self.led_password.text()).encode('utf-8')
            self.btn_next.setEnabled(True)
        else:
            self.btn_next.setEnabled(False)

    def slot_create_wallet(self):
        self.stackedWidget.setCurrentIndex(1)
        self.repaint()  # 立即重绘
        args = ['create', '--client']
        if self.password:
            args.append('--guipassword')
            args.append(self.password)
        seed = self.parent.bwallet_main(*args)
        self.close()
        self.parent.show()
        QTimer.singleShot(0, self.parent.init_daemon)
