# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'create_wallet.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_CreateWallet(object):
    def setupUi(self, CreateWallet):
        CreateWallet.setObjectName(_fromUtf8("CreateWallet"))
        CreateWallet.resize(438, 297)
        self.verticalLayout = QtGui.QVBoxLayout(CreateWallet)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.stackedWidget = QtGui.QStackedWidget(CreateWallet)
        self.stackedWidget.setObjectName(_fromUtf8("stackedWidget"))
        self.page = QtGui.QWidget()
        self.page.setObjectName(_fromUtf8("page"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.page)
        self.verticalLayout_2.setContentsMargins(15, 15, 15, -1)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(-1, -1, -1, 15)
        self.horizontalLayout.setSpacing(15)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.lbl_icon = QtGui.QLabel(self.page)
        self.lbl_icon.setMinimumSize(QtCore.QSize(55, 55))
        self.lbl_icon.setMaximumSize(QtCore.QSize(55, 55))
        self.lbl_icon.setText(_fromUtf8(""))
        self.lbl_icon.setObjectName(_fromUtf8("lbl_icon"))
        self.horizontalLayout.addWidget(self.lbl_icon)
        self.lbl_des = QtGui.QLabel(self.page)
        self.lbl_des.setObjectName(_fromUtf8("lbl_des"))
        self.horizontalLayout.addWidget(self.lbl_des)
        self.horizontalLayout.setStretch(1, 1)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.led_password = QtGui.QLineEdit(self.page)
        self.led_password.setEchoMode(QtGui.QLineEdit.Password)
        self.led_password.setObjectName(_fromUtf8("led_password"))
        self.gridLayout.addWidget(self.led_password, 0, 1, 1, 1)
        self.label = QtGui.QLabel(self.page)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_2 = QtGui.QLabel(self.page)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.led_confirm_password = QtGui.QLineEdit(self.page)
        self.led_confirm_password.setEchoMode(QtGui.QLineEdit.Password)
        self.led_confirm_password.setObjectName(_fromUtf8("led_confirm_password"))
        self.gridLayout.addWidget(self.led_confirm_password, 1, 1, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.frame = QtGui.QFrame(self.page)
        self.frame.setFrameShape(QtGui.QFrame.HLine)
        self.frame.setFrameShadow(QtGui.QFrame.Sunken)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.verticalLayout_2.addWidget(self.frame)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(-1, -1, 20, -1)
        self.horizontalLayout_2.setSpacing(15)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.btn_cancel = QtGui.QPushButton(self.page)
        self.btn_cancel.setMinimumSize(QtCore.QSize(75, 0))
        self.btn_cancel.setMaximumSize(QtCore.QSize(75, 16777215))
        self.btn_cancel.setObjectName(_fromUtf8("btn_cancel"))
        self.horizontalLayout_2.addWidget(self.btn_cancel)
        self.btn_next = QtGui.QPushButton(self.page)
        self.btn_next.setMinimumSize(QtCore.QSize(75, 0))
        self.btn_next.setMaximumSize(QtCore.QSize(75, 16777215))
        self.btn_next.setObjectName(_fromUtf8("btn_next"))
        self.horizontalLayout_2.addWidget(self.btn_next)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtGui.QWidget()
        self.page_2.setObjectName(_fromUtf8("page_2"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.page_2)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.label_3 = QtGui.QLabel(self.page_2)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.verticalLayout_3.addWidget(self.label_3)
        self.stackedWidget.addWidget(self.page_2)
        self.verticalLayout.addWidget(self.stackedWidget)

        self.retranslateUi(CreateWallet)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(CreateWallet)

    def retranslateUi(self, CreateWallet):
        CreateWallet.setWindowTitle(_translate("CreateWallet", "Create wallet", None))
        self.lbl_des.setText(_translate("CreateWallet", "Choose a password to encrypt your wallet keys\n"
"Leave this field empty if you want to disable encryption", None))
        self.label.setText(_translate("CreateWallet", "Password:", None))
        self.label_2.setText(_translate("CreateWallet", "Confirm password:", None))
        self.btn_cancel.setText(_translate("CreateWallet", "Cancel", None))
        self.btn_next.setText(_translate("CreateWallet", "Next", None))
        self.label_3.setText(_translate("CreateWallet", "Uwallet is generating your addresses, please wait...", None))

