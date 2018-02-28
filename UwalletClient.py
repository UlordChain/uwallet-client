# -*- coding: utf-8 -*-
# @Time    : 2017/12/8
# @Author  : Shu
# @Email   : httpservlet@yeah.net


import os, sys

from resource import qrc_resource
from PyQt4.QtCore import QFile
from PyQt4.QtGui import *
from PyQt4.Qt import QLocale, QTranslator
from Forms.mainwindow import BwalletMainWindow



class MyQApplication(QApplication):
    def __init__(self, args):
        super(MyQApplication, self).__init__(args)

        self.qt_tr = None
        self.translator = None
        self.set_style()
        self.set_language()
        self.set_font()

    def set_style(self, filepath=None):
        """ 给应用程序设置style.

        Args:
            filepath: qss文件的路径或者是在资源文件中的表现路径(:/开头)
        Returns:
            None
        Raises:

        """
        if filepath is None:
            # filepath = os.path.join(os.path.dirname(os.path.abspath(__file__)), r'resource\style\bwallet.qss')
            filepath = ":/style/bwallet"  # 正式环境
        self.set_stylesheet(filepath=filepath)

    def set_language(self, lang=None):
        """ 给应用程序设置语言(可以同时加载多个qm文件,比如程序本身的翻译文件, 以及官方提供的右键菜单的翻译文件

        Args:
            lang: 语言代码,比如中国大陆zh-CN,中国台湾zh-TW. 如未设置,则获取本地语言.
                  语言代码参考表[注:QT中使用的是下划线]:
                        http://www.lingoes.cn/zh/translator/langcode.htm
        """
        if lang is None:
            lang = unicode(QLocale.system().name())  # PyQt4.QtCore.QString(u'zh_CN')

        self.translator = QTranslator(self)
        if self.translator.load(':/qm/{}'.format(lang)):
            self.installTranslator(self.translator)

        self.qt_tr = QTranslator(self)
        if self.qt_tr.load(':/qm/qt_{}.qm'.format(lang)):
            self.installTranslator(self.qt_tr)

    def set_stylesheet(self, filepath):
        """ 给控件设置样式

        Args:
            filepath: qss文件的路径
            obj: 要设置style的对象(可以是qApp,或者任意控件对象)
        """
        f = QFile(filepath)
        f.open(QFile.ReadOnly)
        styleSheet = unicode(f.readAll(), encoding='utf8')
        self.setStyleSheet(styleSheet)
        f.close()

    def set_font(self):
        font_id = QFontDatabase.addApplicationFont(":/font/Roboto-Medium")
        font_families = QFontDatabase.applicationFontFamilies(font_id)
        font = QFont()
        font.setFamily(font_families.takeFirst())
        font.setPointSize(10)
        self.setFont(font)


if __name__ == '__main__':

    app = MyQApplication(sys.argv)
    form = BwalletMainWindow({'qt_tr': app.qt_tr, 'translator': app.translator})
    form.show()
    app.exec_()