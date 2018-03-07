# -*- coding: utf-8 -*-
# @Time    : 2017/12/8
# @Author  : Shu
# @Email   : httpservlet@yeah.net
# coding=utf-8
import os
import datetime
import sys

import math
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from FormUI.ui_mainwindow import Ui_bwalletMW
from Forms.create_wallet import CreateWalletDialog
from Forms.title import TitleWidget
from Forms.content import ContentWidget
from Forms.contextmenu import FileMenu, WalletMenu, ViewMenu, ToolsMenu, HelpMenu
from Forms.mengban_setting import SettingtWidget
from Forms.mengban_seed import SeedWidget
from Forms.mengban_password import PasswordWidget
from Forms.system_tray import MySystemTrayIcon
from uwallet.main import main
from Forms.thread_commands import CommandsWalker


class BwalletMainWindow(QMainWindow, Ui_bwalletMW):
    def __init__(self, trans):
        """
        
        :param trans: 语言设置. 一个dict, 包含自定义翻译, 以及系统菜单翻译
        """
        super(BwalletMainWindow, self).__init__()
        self.setupUi(self)
        self.setMinimumSize(QSize(800, 530))
        # 无边框移动相关属性
        self.mouse_press_status = False
        self.startPos = self.pos()
        # 无边框窗体使用系统系统函数最大化以后,会遮盖任务栏
        # 自己重写此功能
        self.ismaxsize = False  # 标志窗口是否最大化
        self.geo = self.geometry()

        # trans把两个语言翻译传入进来, 使得运行后还能删除刚开始设置的语言设置
        self.qt_tr = trans.get('qt_tr')
        self.translator = trans.get('translator')
        self.setWindowFlags(Qt.FramelessWindowHint)  # 设置无边框
        self.setAttribute(Qt.WA_TranslucentBackground,True)
        #self.setStyleSheet("background-color:#2C3E50;")
        # self.setWindowOpacity(0.5)  # 设置透明 (0~1),1为不透明
        # 布局
        self.title_widget = TitleWidget(self)
        self.content_widget = ContentWidget(self)
        main_layout = QVBoxLayout()
        main_layout.addWidget(self.title_widget)
        main_layout.addWidget(self.content_widget)
        main_layout.setSpacing(0)
        main_layout.setContentsMargins(0, 0, 0, 0)
        self.centralwidget.setLayout(main_layout)

        button_list = [self.title_widget.tbt_history, self.title_widget.tbt_send, self.title_widget.tbt_receive,
                       self.title_widget.tbt_addresses]

        signal_mapper = QSignalMapper(self)
        for i, button in enumerate(button_list):
            button.clicked.connect(signal_mapper.map)
            signal_mapper.setMapping(button, i)
        signal_mapper.mapped.connect(self.slot_turn_page)

        # 去除状态没有了缩放效果(QSizeGrip[状态栏自带]可用于自定义缩放)
        self.size_grip = QSizeGrip(self)
        self.size_grip.resize(20, 20)
        # 设置缩放控件透明度
        opacityEffect = QGraphicsOpacityEffect()
        self.size_grip.setGraphicsEffect(opacityEffect)
        opacityEffect.setOpacity(0.7)

        # 自定义菜单栏
        self.button_list = [self.title_widget.btn_file, self.title_widget.btn_wallet, self.title_widget.btn_view,
                            self.title_widget.btn_tools, self.title_widget.btn_help]
        signal_mapper = QSignalMapper(self)
        for i, button in enumerate(self.button_list):
            # 其实不需要这么复杂, 直接使用QPushButton.setMenu()就可以
            # http://blog.csdn.net/u011417605/article/details/51218493
            button.clicked.connect(signal_mapper.map)
            signal_mapper.setMapping(button, i)
        signal_mapper.mapped.connect(self.slot_menu_bar)

        self.title_widget.btn_close.clicked.connect(self.close)
        self.title_widget.btn_min.clicked.connect(self.slot_minimize)
        self.title_widget.btn_max.clicked.connect(self.slot_maximize)

        self.title_widget.btn_setting.clicked.connect(self.slot_settings)
        self.title_widget.btn_seed.clicked.connect(self.slot_getseed)
        self.title_widget.btn_password.clicked.connect(self.slot_password)

        self.init_systemtray()

        self.command_walker = CommandsWalker(interval=3, filter_1='--receiving', parent=self)
        self.connect(self.command_walker, SIGNAL('daemon'), self.slot_check_daemon, Qt.AutoConnection)
        self.connect(self.command_walker, SIGNAL('address'), self.slot_address, Qt.AutoConnection)
        self.connect(self.command_walker, SIGNAL('history'), self.slot_history, Qt.AutoConnection)
        self.connect(self.command_walker, SIGNAL('balance'), self.slot_balance, Qt.AutoConnection)

        self.title_widget.btn_file.setVisible(False)
        self.title_widget.btn_wallet.setVisible(False)
        self.title_widget.btn_view.setVisible(False)
        self.title_widget.btn_tools.setVisible(False)
        self.title_widget.btn_help.setVisible(False)

        self.setWindowIcon(QIcon(":/images/ico"))

        QTimer.singleShot(0, self.init_check)

        langindx = self.read_language_conf()

        # lang = 'zh_CN'
        # if langindx =='0':
        #     lang ='en_US'
        # self.qt_tr = QTranslator()
        # if self.qt_tr.load(':/qm/qt_{}.qm'.format(lang)):
        #     QApplication.installTranslator(self.qt_tr)
        #
        # self.translator = QTranslator()
        # if self.translator.load(':/qm/{}'.format(lang)):
        #     QApplication.installTranslator(self.translator)
    ################################## 初始化相关 ##################################

    def paintEvent(self,event):
        m = 1

        path = QPainterPath()
        path.setFillRule(Qt.WindingFill)
        path.addRect(m, m, self.width()-m*2, self.height()-m*2)

        painter = QPainter(self)
        #painter.drawLine(QLineF)
        #painter.setRenderHint(QPainter.Antialiasing, True)
        painter.fillPath(path, QBrush(Qt.white))

        color = QColor(100, 100, 100, 30)
        #for(int i=0; i<10; i++)

        for i in range(m):
            path = QPainterPath()
            path.setFillRule(Qt.WindingFill)
            path.addRoundRect(m-i, m-i, self.width()-(m-i)*2, self.height()-(m-i)*2,1,1)
            color.setAlpha(90 - math.sqrt(i)*30)
            painter.setPen(QPen(color,1,Qt.SolidLine))
            painter.drawRoundRect(QRect(m-i, m-i, self.width()-(m-i)*2, self.height()-(m-i)*2), 0,0)

#             path = QPainterPath()
#             path.setFillRule(Qt.WindingFill)
#             path.addRect(m-i, m-i, self.width()-(m-i)*2, self.height()-(m-i)*2)
#             color.setAlpha(90 - math.sqrt(i)*30)
#             painter.setPen(QPen(color,1))
#             painter.drawPath(path

    def init_check(self):
        """初始化主窗口时, 检查钱包是否存在"""
        if not self.bwallet_main('haswallet', '--client'):  # 如果没有钱包
            self.hide()
            create_dialog = CreateWalletDialog(self)
            create_dialog.show()
        else:
            QTimer.singleShot(0, self.init_daemon)

    def init_systemtray(self):
        """ 初始化托盘图标 """
        self.tray = MySystemTrayIcon(self)
        self.tray.setIcon(QIcon(":/images/ico"))
        self.tray.setToolTip(self.tr(u"UWallet client"))
        self.tray.activated.connect(self.slot_systemtray)
        self.tray.show()

    def init_daemon(self):
        """启动daemon"""
        # daemon不能在线程中启动, 不然各种奇怪的问题, 比如修改密码
        # self.bwallet_main('daemon', 'start', '--client')
        import multiprocessing
        sys.argv=sys.argv[:1]
        sys.argv.append('daemon')
        sys.argv.append('start')
        multiprocessing.Process(target=main).start()
        self.command_walker.start()

    ################################## 通用方法 ##################################
    def bwallet_main(self, *args, **kwargs):
        """ 因为钱包的各种命令是线程不安全的, 所以为了安全的执行某条命令
        在执行的时候, 最好是停止其他执行线程
        
        kwargs: 会传入 thread_safe=True
        表明需要先停止线程, 执行命令, 然后再启动线程
        """
        thread_safe = kwargs.get('thread_safe')
        sys.argv = sys.argv[:1]
        for arg in args:
            sys.argv.append(arg)
        if thread_safe is True:
            if self.command_walker.isRunning():
                self.command_walker.stop()
                self.command_walker.wait()

        rs = main()

        if thread_safe is True:
            self.command_walker.start()
            while True:
                # 防止两次停止/启动间隔太近,导致阻塞的问题
                # 第二次停止调用stop时,设置stopped为True,有可能在第一次线程运行initialize之前
                # 此时:initialize后运行, isStopped就为False,线程就不会退出
                # 导致stopped一直是False, wait就一直处于阻塞状态
                if self.command_walker.isStopped() == False:
                    break

        return rs

    def is_title(self, xPos, yPos):
        size = self.size()
        x = size.width()
        y = size.height()
        return yPos < 30 and xPos < x - 120

    def set_size(self):
        """mainwindow改变大小时, 修改其子控件大小"""
        self.title_widget.setGeometry(0, 0, self.width(), 87)
        self.content_widget.setGeometry(0, 87, self.width(), self.height() - 87)
        self.set_grip_size()
        self.set_mengban_size()

    def set_grip_size(self):
        """设置缩放按钮到主程序的右下角(default:左上角)"""
        self.size_grip.setGeometry(self.width() - 20, self.height() - 20, 20, 20)

    def set_mengban_size(self, widget=None):
        """设置setting面板缩放操作, 以及缩放按钮置顶"""
        if isinstance(widget, QWidget):
            widget.setGeometry(0, 35, self.width() - 2, self.height() - 35 - 2)  # 35的y是要让最大化, 最小化, 关闭按钮可以点击
        else:
            if hasattr(self, 'setting') and isinstance(self.setting, QWidget) and self.setting.isVisible():
                self.setting.setGeometry(0, 35, self.width() - 2, self.height() - 35 - 2)
            elif hasattr(self, 'getseed') and isinstance(self.getseed, QWidget) and self.getseed.isVisible():
                self.getseed.setGeometry(0, 35, self.width() - 2, self.height() - 35 - 2)
            elif hasattr(self, 'password') and isinstance(self.password, QWidget) and self.password.isVisible():
                self.password.setGeometry(0, 35, self.width() - 2, self.height() - 35 - 2)

        self.size_grip.raise_()  # 让右下角缩放小图标位于所有控件之上

    def stop_daemon(self):
        """停止daemon服务"""
        self.bwallet_main('daemon', 'stop', '--client')

    def read_language_conf(self):
        langPath = os.path.abspath('.') + '\language.txt'
        if not os.path.exists(langPath):
            f=file(langPath, "w+")
            f.write('1')
            f.close()
        file_object = open(langPath, "r")
        lang = file_object.read( )
        file_object.close( )
        return lang

    def write_language_conf(self,lang):
        try:
            langPath = os.path.abspath('.') + '\language.txt'
            if not os.path.exists(langPath):
                f=file(langPath, "w+")
                f.write(lang)
                f.close()
            else:
                file_object = open(langPath, "w+")
                file_object.write(lang)
                file_object.close( )
        except Exception,e:
            print e

    ################################## 槽函数 ##################################
    def slot_change_lang(self, index):
        """设置语言槽函数"""
        index = str(index)
        lang = ''
        if index == '0':
            lang = 'en_US'
        elif index == '1':
            lang = 'zh_CN'
        self.write_language_conf(index)

        # 每次设置语言之前, 删掉上一次设置的语言
        if isinstance(self.qt_tr, QTranslator):
            QApplication.removeTranslator(self.qt_tr)
        if isinstance(self.translator, QTranslator):
            QApplication.removeTranslator(self.translator)

        self.qt_tr = QTranslator()
        if self.qt_tr.load(':/qm/qt_{}.qm'.format(lang)):
            QApplication.installTranslator(self.qt_tr)

        self.translator = QTranslator()
        if self.translator.load(':/qm/{}'.format(lang)):
            QApplication.installTranslator(self.translator)

        self.retranslateUi(self)
        self.title_widget.retranslateUi(self.title_widget)
        self.content_widget.retranslateUi(self.content_widget)
        self.content_widget.custom_retranslateUi()
        self.setting.retranslateUi(self.setting)

        if hasattr(self, 'getseed'):
            self.getseed.retranslateUi(self.getseed)
        if hasattr(self, 'password'):
            self.password.retranslateUi(self.password)
        self.tray.retranslateUi()

    def slot_minimize(self):
        self.showMinimized()

    def slot_maximize(self):
        if self.ismaxsize:
            self.setGeometry(self.geo)
            self.ismaxsize = False
        else:
            self.geo = self.geometry()
            self.setGeometry(QApplication.desktop().availableGeometry())
            self.ismaxsize = True

    def slot_turn_page(self, current_index):
        self.content_widget.stackedWidget.setCurrentIndex(current_index + 1)

    def slot_menu_bar(self, current_index):
        p = self.mapToGlobal(QPoint())  # 找到主窗口的全局坐标
        wd = self.button_list[current_index].geometry()  # 获取菜单按钮的位置以及大小

        file_menu = FileMenu(self)
        wallet_menu = WalletMenu(self)
        view_menu = ViewMenu(self)
        tools_menu = ToolsMenu(self)
        help_menu = HelpMenu(self)
        menu_list = [file_menu, wallet_menu, view_menu, tools_menu, help_menu]
        menu = menu_list[current_index]
        menu.exec_(QPoint(p.x() + wd.x(), p.y() + 87))

    def slot_settings(self):
        if not (hasattr(self, 'setting') and isinstance(self.setting, QWidget)):
            self.setting = SettingtWidget(self)
            self.setting.btn_setting_appearance_close.clicked.connect(self.setting.close)
            self.setting.cbx_setting_appearance_language.currentIndexChanged.connect(self.slot_change_lang)
        if not self.setting.isVisible():
            self.setting.show()
            lang = unicode(QLocale.system().name())
            # if lang == 'zh_CN':
            #     self.setting.cbx_setting_appearance_language.setCurrentIndex(1)
            # else:
            #     self.setting.cbx_setting_appearance_language.setCurrentIndex(0)
            self.setting.btn_setting_appearance_close.setFocus(True)
            # self.setting.btn_setting_appearance_close.setShortcut(QKeySequence.InsertParagraphSeparator)
            # self.setting.btn_setting_appearance_close.setShortcut(Qt.Key_Enter | Qt.Key_Return)
            self.set_mengban_size(self.setting)

    def slot_getseed(self):
        if not (hasattr(self, 'getseed') and isinstance(self.getseed, QWidget)):
            self.getseed = SeedWidget(self)
            self.getseed.btn_seed_close.clicked.connect(self.getseed.close)
        if not self.getseed.isVisible():
            self.getseed.show()
            self.getseed.led_seed_password.setText('')
            is_password = self.bwallet_main('haspassword', '--client', thread_safe=True)

            if is_password is True:
                self.getseed.ted_setting_getseed.setVisible(False)
                self.getseed.led_seed_password.setVisible(True)
                self.getseed.btn_seed_password.setVisible(True)
            else:
                self.getseed.ted_setting_getseed.setVisible(True)
                self.getseed.led_seed_password.setVisible(False)
                self.getseed.btn_seed_password.setVisible(False)
                try:
                    rs = self.bwallet_main('getseed', '--client', thread_safe=True)
                except Exception as e:
                    print (e)
                else:
                    self.getseed.ted_setting_getseed.setText(rs)
            self.set_mengban_size()

    def slot_password(self):
        if not (hasattr(self, 'password') and isinstance(self.password, QWidget)):
            self.password = PasswordWidget(self)
        if not self.password.isVisible():
            self.password.show()
            self.password.led_password_current.setText('')
            self.password.led_password_new.setText('')
            self.password.led_password_comfirm.setText('')
            is_password = self.bwallet_main('haspassword', '--client', thread_safe=True)
            if is_password is True:
                self.password.lbl_password_current.setVisible(True)
                self.password.led_password_current.setVisible(True)
                self.password.lbl_password_des.setText(self.tr(
                    """Your bnc are password protected. \nHowever, your wallet file is not encrypted. \nUse this dialog to change your passowrd."""))
            else:
                self.password.lbl_password_current.setVisible(False)
                self.password.led_password_current.setVisible(False)
                self.password.lbl_password_des.setText(
                    self.tr("""Your wallet is not protected. \nUse this dialog to add a password to your wallet."""))
            self.set_mengban_size()

    def slot_systemtray(self, reason):
        """ 系统托盘操作的槽函数 """
        if reason == QSystemTrayIcon.DoubleClick:
            if self.isVisible():
                self.hide()
            else:
                self.show()

    def slot_check_daemon(self, status):
        """检查daemon状态的槽函数"""
        if status is True:
            style = """border-image: url(:/images/greenball);"""
        else:
            style = """border-image: url(:/images/redball);"""
        self.title_widget.btn_network.setStyleSheet(style)

    def slot_address(self, listaddresses, cur_addr):
        """绑定address数据"""
        # clear发射itemSelectionChanged信号
        self.content_widget.twd_addresses.clear()

        cur_item = None
        for i, addr_balance in enumerate(listaddresses):
            ab = addr_balance.split(',')
            addr = ab[0].strip()
            balance = ab[1].strip()
            if balance.endswith('.'):
                balance = balance[:-1]
            view_list = [addr, balance]
            item = QTreeWidgetItem(self.content_widget.twd_addresses, view_list)
            item.setData(0, Qt.UserRole, QVariant(addr))
            if self.content_widget.led_receiving_address.text().isEmpty():
                self.content_widget.led_receiving_address.setText(addr)

            if addr == cur_addr:
                cur_item = item

        if cur_item:
            cur_item.setSelected(True)

        update_dt = str(datetime.datetime.now()).split('.')[0]
        self.content_widget.lbl_address_updatetime.setText(update_dt)

    def slot_history(self, historys, cur_txid):
        """绑定history数据"""
        self.content_widget.twd_history.clear()

        cur_item = None
        temps = []
        for history in historys:
            if not isinstance(history, dict):
                # 第一次返回的数据是listaddresses命令的数据, 不知道为什么
                return
            fee = history.get('fee')
            value = history.get('value')
            if value < 0:
                amount = value + fee
            else:
                amount = value
            dt = history.get('date').strip()
            if dt == '----':
                dt = self.tr('unconfirmed')  # 未确认交易
            txid = history.get('txid').strip()
            view_list = [dt, str(amount), str(fee)]

            item = QTreeWidgetItem(self.content_widget.twd_history, view_list)
            item.setData(0, Qt.UserRole, QVariant(txid))

            if txid == cur_txid:
                cur_item = item

            if value >= 0:
                item_column_count = range(item.columnCount())
                for i in item_column_count:
                    item.setForeground(i, QBrush(QColor(0, 128, 0, 160)))

        if cur_item:
            cur_item.setSelected(True)

        update_dt = str(datetime.datetime.now()).split('.')[0]
        self.content_widget.lbl_history_updatetime.setText(update_dt)

    def slot_balance(self, balance):

        self.title_widget.lbl_balance.setText(balance)

    ##################################  重写系统事件 ##################################
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.mouse_press_status = True
            self.startPos = event.globalPos() - self.frameGeometry().topLeft()

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.mouse_press_status = False

    def mouseMoveEvent(self, event):
        if not self.ismaxsize:
            if event.buttons() == Qt.LeftButton and self.mouse_press_status is True:
                self.move(event.globalPos() - self.startPos)

    def mouseDoubleClickEvent(self, event):
        if event.button() == Qt.LeftButton:
            point = self.mapFromGlobal(QCursor().pos())
            if self.is_title(point.x(), point.y()):
                self.slot_maximize()

    def resizeEvent(self, event):
        self.set_size()

    # def showEvent(self, *args, **kwargs):
    #     self.slot_change_lang('0')

    def closeEvent(self, event):
        """ 重写关闭事件 """
        # 关闭对应服务
        self.tray.hide()  # 隐藏托盘图标
        # 不用手工关闭, 钱包模块已经实现了干净的关闭daemon线程的操作
        self.stop_daemon()  # 关闭daemon服务
        if self.command_walker.isRunning():
            self.command_walker.stop()
            self.command_walker.wait()
            # self.close()
            # self.close()
            # sys.exit(0)  # 感觉退出更快,不知道有什么隐患没有
            # QTimer.singleShot(0, qApp, SLOT("quit()"))

    def keyPressEvent(self, event):
        """ 按下esc键, 实现与关闭按钮同样的效果 """
        if event.key() == Qt.Key_Escape:
            if hasattr(self, 'setting') and isinstance(self.setting, QWidget) and self.setting.isVisible():
                self.setting.close()
            elif hasattr(self, 'getseed') and isinstance(self.getseed, QWidget) and self.getseed.isVisible():
                self.getseed.close()
            elif hasattr(self, 'password') and isinstance(self.password, QWidget) and self.password.isVisible():
                self.password.close()
        else:
            QMainWindow.keyPressEvent(self, event)

    def eventFilter(self, obj, event):
        if isinstance(obj, QFrame):
            if unicode(obj.objectName()).encode('u8') in ['frame_left', 'frame_top']:
                if event.type() == QEvent.MouseButtonPress:
                    obj.parent().close()
                    return True
        return False