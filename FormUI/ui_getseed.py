# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'getseed.ui'
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

class Ui_getseedWD(object):
    def setupUi(self, getseedWD):
        getseedWD.setObjectName(_fromUtf8("getseedWD"))
        getseedWD.resize(876, 517)
        self.verticalLayout = QtGui.QVBoxLayout(getseedWD)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.frame_top = QtGui.QFrame(getseedWD)
        self.frame_top.setMinimumSize(QtCore.QSize(0, 52))
        self.frame_top.setMaximumSize(QtCore.QSize(16777215, 52))
        self.frame_top.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_top.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_top.setObjectName(_fromUtf8("frame_top"))
        self.verticalLayout.addWidget(self.frame_top)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.frame_left = QtGui.QFrame(getseedWD)
        self.frame_left.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_left.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_left.setObjectName(_fromUtf8("frame_left"))
        self.horizontalLayout_4.addWidget(self.frame_left)
        self.frame_rigth = QtGui.QFrame(getseedWD)
        self.frame_rigth.setMinimumSize(QtCore.QSize(400, 0))
        self.frame_rigth.setMaximumSize(QtCore.QSize(400, 16777215))
        self.frame_rigth.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_rigth.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_rigth.setObjectName(_fromUtf8("frame_rigth"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.frame_rigth)
        self.verticalLayout_2.setMargin(15)
        self.verticalLayout_2.setSpacing(10)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.label = QtGui.QLabel(self.frame_rigth)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout_2.addWidget(self.label)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setSpacing(10)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.led_seed_password = QtGui.QLineEdit(self.frame_rigth)
        self.led_seed_password.setEchoMode(QtGui.QLineEdit.Password)
        self.led_seed_password.setObjectName(_fromUtf8("led_seed_password"))
        self.horizontalLayout_3.addWidget(self.led_seed_password)
        self.btn_seed_password = QtGui.QPushButton(self.frame_rigth)
        self.btn_seed_password.setMinimumSize(QtCore.QSize(106, 0))
        self.btn_seed_password.setMaximumSize(QtCore.QSize(106, 16777215))
        self.btn_seed_password.setObjectName(_fromUtf8("btn_seed_password"))
        self.horizontalLayout_3.addWidget(self.btn_seed_password)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.ted_setting_getseed = QtGui.QTextEdit(self.frame_rigth)
        self.ted_setting_getseed.setMinimumSize(QtCore.QSize(0, 80))
        self.ted_setting_getseed.setMaximumSize(QtCore.QSize(16777215, 80))
        self.ted_setting_getseed.setObjectName(_fromUtf8("ted_setting_getseed"))
        self.verticalLayout_2.addWidget(self.ted_setting_getseed)
        self.label_2 = QtGui.QLabel(self.frame_rigth)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout_2.addWidget(self.label_2)
        self.label_3 = QtGui.QLabel(self.frame_rigth)
        self.label_3.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.verticalLayout_2.addWidget(self.label_3)
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setContentsMargins(35, 10, -1, -1)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.label_4 = QtGui.QLabel(self.frame_rigth)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.verticalLayout_3.addWidget(self.label_4)
        self.label_5 = QtGui.QLabel(self.frame_rigth)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.verticalLayout_3.addWidget(self.label_5)
        self.label_6 = QtGui.QLabel(self.frame_rigth)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.verticalLayout_3.addWidget(self.label_6)
        self.verticalLayout_2.addLayout(self.verticalLayout_3)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.btn_seed_close = QtGui.QPushButton(self.frame_rigth)
        self.btn_seed_close.setMinimumSize(QtCore.QSize(106, 0))
        self.btn_seed_close.setMaximumSize(QtCore.QSize(106, 16777215))
        self.btn_seed_close.setObjectName(_fromUtf8("btn_seed_close"))
        self.horizontalLayout.addWidget(self.btn_seed_close)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_4.addWidget(self.frame_rigth)
        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.retranslateUi(getseedWD)
        QtCore.QMetaObject.connectSlotsByName(getseedWD)

    def retranslateUi(self, getseedWD):
        getseedWD.setWindowTitle(_translate("getseedWD", "Form", None))
        self.label.setText(_translate("getseedWD", "Your wallet generation seed is :", None))
        self.led_seed_password.setPlaceholderText(_translate("getseedWD", "Please enter your password: ", None))
        self.btn_seed_password.setText(_translate("getseedWD", "OK", None))
        self.label_2.setText(_translate("getseedWD", "Please save these 13 words on paper (order is important). \n"
"This seed will allow you to recover your wallet in case \n"
"of computer failure.", None))
        self.label_3.setText(_translate("getseedWD", "WARNING: ", None))
        self.label_4.setText(_translate("getseedWD", "1.Never disclose your seed.", None))
        self.label_5.setText(_translate("getseedWD", "2.Never type it on a website", None))
        self.label_6.setText(_translate("getseedWD", "3.Do not store it electronically", None))
        self.btn_seed_close.setText(_translate("getseedWD", "close", None))

