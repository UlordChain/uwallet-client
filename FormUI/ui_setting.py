# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'setting.ui'
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

class Ui_settingWD(object):
    def setupUi(self, settingWD):
        settingWD.setObjectName(_fromUtf8("settingWD"))
        settingWD.resize(876, 517)
        self.verticalLayout = QtGui.QVBoxLayout(settingWD)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.frame_top = QtGui.QFrame(settingWD)
        self.frame_top.setMinimumSize(QtCore.QSize(0, 52))
        self.frame_top.setMaximumSize(QtCore.QSize(16777215, 52))
        self.frame_top.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_top.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_top.setObjectName(_fromUtf8("frame_top"))
        self.verticalLayout.addWidget(self.frame_top)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.frame_left = QtGui.QFrame(settingWD)
        self.frame_left.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_left.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_left.setObjectName(_fromUtf8("frame_left"))
        self.horizontalLayout_4.addWidget(self.frame_left)
        self.frame_rigth = QtGui.QFrame(settingWD)
        self.frame_rigth.setMinimumSize(QtCore.QSize(400, 0))
        self.frame_rigth.setMaximumSize(QtCore.QSize(400, 16777215))
        self.frame_rigth.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_rigth.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_rigth.setObjectName(_fromUtf8("frame_rigth"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.frame_rigth)
        self.verticalLayout_2.setContentsMargins(10, 10, 10, 0)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(-1, -1, -1, 10)
        self.horizontalLayout.setSpacing(15)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.btn_setting_appearance = QtGui.QPushButton(self.frame_rigth)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.btn_setting_appearance.setFont(font)
        self.btn_setting_appearance.setFlat(True)
        self.btn_setting_appearance.setObjectName(_fromUtf8("btn_setting_appearance"))
        self.horizontalLayout.addWidget(self.btn_setting_appearance)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(10, -1, 15, -1)
        self.horizontalLayout_2.setSpacing(10)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label = QtGui.QLabel(self.frame_rigth)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_2.addWidget(self.label)
        self.cbx_setting_appearance_language = QtGui.QComboBox(self.frame_rigth)
        self.cbx_setting_appearance_language.setObjectName(_fromUtf8("cbx_setting_appearance_language"))
        self.cbx_setting_appearance_language.addItem(_fromUtf8(""))
        self.cbx_setting_appearance_language.addItem(_fromUtf8(""))
        self.horizontalLayout_2.addWidget(self.cbx_setting_appearance_language)
        self.horizontalLayout_2.setStretch(1, 1)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem2)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(-1, -1, 20, 10)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem3)
        self.btn_setting_appearance_close = QtGui.QPushButton(self.frame_rigth)
        self.btn_setting_appearance_close.setMinimumSize(QtCore.QSize(106, 0))
        self.btn_setting_appearance_close.setMaximumSize(QtCore.QSize(106, 16777215))
        self.btn_setting_appearance_close.setAutoDefault(True)
        self.btn_setting_appearance_close.setDefault(True)
        self.btn_setting_appearance_close.setObjectName(_fromUtf8("btn_setting_appearance_close"))
        self.horizontalLayout_3.addWidget(self.btn_setting_appearance_close)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4.addWidget(self.frame_rigth)
        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.retranslateUi(settingWD)
        QtCore.QMetaObject.connectSlotsByName(settingWD)

    def retranslateUi(self, settingWD):
        settingWD.setWindowTitle(_translate("settingWD", "Form", None))
        self.btn_setting_appearance.setText(_translate("settingWD", "Appearance", None))
        self.label.setText(_translate("settingWD", "Language:", None))
        self.cbx_setting_appearance_language.setItemText(0, _translate("settingWD", "English", None))
        self.cbx_setting_appearance_language.setItemText(1, _translate("settingWD", "简体中文", None))
        self.btn_setting_appearance_close.setText(_translate("settingWD", "close", None))

