# -*- coding: utf-8 -*-
# @Author       : Shu
# @Email        : httpservlet@yeah.net
# @Date         : 2017/12/27
# @Description  :
from PyQt4.QtGui import *
from PyQt4.QtCore import *
import qrcode


class QRCodeWidget(QWidget):
    def __init__(self, data=None, fixedSize=False, parent=None):
        super(QRCodeWidget,self).__init__(parent=parent)
        self.data = None
        self.qr = None
        self.fixedSize = fixedSize
        if fixedSize:
            self.setFixedSize(fixedSize, fixedSize)
        self.setData(data)

    def setData(self, data):
        if self.data != data:
            self.data = data
        if self.data:
            self.qr = qrcode.QRCode()
            self.qr.add_data(self.data)
            if not self.fixedSize:
                k = len(self.qr.get_matrix())
                self.setMinimumSize(k * 5, k * 5)
        else:
            self.qr = None
        self.update()

    def paintEvent(self, e):
        if not self.data:
            return

        black = QColor(0, 0, 0, 255)
        white = QColor(255, 255, 255, 255)

        if not self.qr:
            qp = QPainter()
            qp.begin(self)
            qp.setBrush(white)
            qp.setPen(white)
            r = qp.viewport()
            qp.drawRect(0, 0, r.width(), r.height())
            qp.end()
            return

        matrix = self.qr.get_matrix()
        k = len(matrix)
        qp = QPainter()
        qp.begin(self)
        r = qp.viewport()

        margin = 10
        framesize = min(r.width(), r.height())
        boxsize = int((framesize - 2 * margin) / k)
        size = k * boxsize
        left = (r.width() - size) / 2
        top = (r.height() - size) / 2

        # Make a white margin around the QR in case of dark theme use
        qp.setBrush(white)
        qp.setPen(white)
        qp.drawRect(left - margin, top - margin, size + (margin * 2), size + (margin * 2))
        qp.setBrush(black)
        qp.setPen(black)

        for r in range(k):
            for c in range(k):
                if matrix[r][c]:
                    qp.drawRect(left + c * boxsize, top + r * boxsize, boxsize - 1, boxsize - 1)
        qp.end()
