# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
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

class Ui_bwalletMW(object):
    def setupUi(self, bwalletMW):
        bwalletMW.setObjectName(_fromUtf8("bwalletMW"))
        bwalletMW.resize(800, 530)
        self.centralwidget = QtGui.QWidget(bwalletMW)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        bwalletMW.setCentralWidget(self.centralwidget)

        self.retranslateUi(bwalletMW)
        QtCore.QMetaObject.connectSlotsByName(bwalletMW)

    def retranslateUi(self, bwalletMW):
        bwalletMW.setWindowTitle(_translate("bwalletMW", "uwallet", None))

