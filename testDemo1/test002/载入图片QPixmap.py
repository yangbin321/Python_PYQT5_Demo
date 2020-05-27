#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author : yangbin
# @Time : 2020/5/24 10:20
# @File : 载入图片QPixmap.py
# @Describe ：

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton
from PyQt5.QtGui import QPixmap


class myClass(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("载入图片控件QPixmap")
        self.setGeometry(700, 400, 600, 500)
        # 图片的载体
        self.labl = QLabel("图片", self)
        self.labl.resize(600, 350)       # 设置label大小
        # 图片的载入
        self.pm = QPixmap("./img/2.jpg")
        self.labl.setPixmap(self.pm)
        self.labl.setScaledContents(True)        # 设置图片的大小和载体的尺寸一样

        # 移除按钮
        btn1 = QPushButton("移除图片", self)
        btn1.clicked.connect(self.myRemoveP)
        btn1.move(150, 370)
        # 增加按钮
        btn2 = QPushButton("增加图片", self)
        btn2.clicked.connect(self.myAddP)
        btn2.move(350, 370)

        self.show()

    def myRemoveP(self):
        self.labl.setPixmap(QPixmap(""))

    def myAddP(self):
        self.labl.setPixmap(QPixmap(self.pm))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mc = myClass()
    sys.exit(app.exec_())
