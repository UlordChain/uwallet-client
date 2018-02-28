# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'update_password.ui'
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

class Ui_updatepasswordWD(object):
    def setupUi(self, updatepasswordWD):
        updatepasswordWD.setObjectName(_fromUtf8("updatepasswordWD"))
        updatepasswordWD.resize(876, 517)
        self.verticalLayout = QtGui.QVBoxLayout(updatepasswordWD)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.frame_top = QtGui.QFrame(updatepasswordWD)
        self.frame_top.setMinimumSize(QtCore.QSize(0, 52))
        self.frame_top.setMaximumSize(QtCore.QSize(16777215, 52))
        self.frame_top.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_top.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_top.setObjectName(_fromUtf8("frame_top"))
        self.verticalLayout.addWidget(self.frame_top)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.frame_left = QtGui.QFrame(updatepasswordWD)
        self.frame_left.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_left.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_left.setObjectName(_fromUtf8("frame_left"))
        self.horizontalLayout_4.addWidget(self.frame_left)
        self.frame_rigth = QtGui.QFrame(updatepasswordWD)
        self.frame_rigth.setMinimumSize(QtCore.QSize(400, 0))
        self.frame_rigth.setMaximumSize(QtCore.QSize(400, 16777215))
        self.frame_rigth.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_rigth.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_rigth.setObjectName(_fromUtf8("frame_rigth"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.frame_rigth)
        self.verticalLayout_2.setMargin(15)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.lbl_password_icon = QtGui.QLabel(self.frame_rigth)
        self.lbl_password_icon.setMinimumSize(QtCore.QSize(70, 70))
        self.lbl_password_icon.setMaximumSize(QtCore.QSize(70, 70))
        self.lbl_password_icon.setText(_fromUtf8(""))
        self.lbl_password_icon.setPixmap(QtGui.QPixmap(_fromUtf8("C:/Users/Administrator/Desktop/123/第二版/02切图/password1.png")))
        self.lbl_password_icon.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_password_icon.setObjectName(_fromUtf8("lbl_password_icon"))
        self.horizontalLayout.addWidget(self.lbl_password_icon)
        self.lbl_password_des = QtGui.QLabel(self.frame_rigth)
        self.lbl_password_des.setText(_fromUtf8(""))
        self.lbl_password_des.setObjectName(_fromUtf8("lbl_password_des"))
        self.horizontalLayout.addWidget(self.lbl_password_des)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setHorizontalSpacing(15)
        self.gridLayout.setVerticalSpacing(10)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.lbl_password_current = QtGui.QLabel(self.frame_rigth)
        self.lbl_password_current.setObjectName(_fromUtf8("lbl_password_current"))
        self.gridLayout.addWidget(self.lbl_password_current, 0, 0, 1, 1)
        self.label_4 = QtGui.QLabel(self.frame_rigth)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 1, 0, 1, 1)
        self.label_5 = QtGui.QLabel(self.frame_rigth)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout.addWidget(self.label_5, 2, 0, 1, 1)
        self.led_password_current = QtGui.QLineEdit(self.frame_rigth)
        self.led_password_current.setEchoMode(QtGui.QLineEdit.Password)
        self.led_password_current.setObjectName(_fromUtf8("led_password_current"))
        self.gridLayout.addWidget(self.led_password_current, 0, 1, 1, 1)
        self.led_password_new = QtGui.QLineEdit(self.frame_rigth)
        self.led_password_new.setEchoMode(QtGui.QLineEdit.Password)
        self.led_password_new.setObjectName(_fromUtf8("led_password_new"))
        self.gridLayout.addWidget(self.led_password_new, 1, 1, 1, 1)
        self.led_password_comfirm = QtGui.QLineEdit(self.frame_rigth)
        self.led_password_comfirm.setEchoMode(QtGui.QLineEdit.Password)
        self.led_password_comfirm.setObjectName(_fromUtf8("led_password_comfirm"))
        self.gridLayout.addWidget(self.led_password_comfirm, 2, 1, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(10)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.btn_passwod_ok = QtGui.QPushButton(self.frame_rigth)
        self.btn_passwod_ok.setMinimumSize(QtCore.QSize(106, 0))
        self.btn_passwod_ok.setMaximumSize(QtCore.QSize(106, 16777215))
        self.btn_passwod_ok.setObjectName(_fromUtf8("btn_passwod_ok"))
        self.horizontalLayout_2.addWidget(self.btn_passwod_ok)
        self.btn_password_close = QtGui.QPushButton(self.frame_rigth)
        self.btn_password_close.setMinimumSize(QtCore.QSize(106, 0))
        self.btn_password_close.setMaximumSize(QtCore.QSize(106, 16777215))
        self.btn_password_close.setObjectName(_fromUtf8("btn_password_close"))
        self.horizontalLayout_2.addWidget(self.btn_password_close)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_4.addWidget(self.frame_rigth)
        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.retranslateUi(updatepasswordWD)
        QtCore.QMetaObject.connectSlotsByName(updatepasswordWD)

    def retranslateUi(self, updatepasswordWD):
        updatepasswordWD.setWindowTitle(_translate("updatepasswordWD", "Form", None))
        self.lbl_password_current.setText(_translate("updatepasswordWD", "Current Password:", None))
        self.label_4.setText(_translate("updatepasswordWD", "New Password:", None))
        self.label_5.setText(_translate("updatepasswordWD", "Confirm Password:", None))
        self.btn_passwod_ok.setText(_translate("updatepasswordWD", "OK", None))
        self.btn_password_close.setText(_translate("updatepasswordWD", "Close", None))

