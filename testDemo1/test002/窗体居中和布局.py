#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author : yangbin
# @Time : 2020/5/23 9:34
# @File : 窗体居中和布局.py
# @Describe ：

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel


class MyForm1(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("窗体居中布局")
        lb1 = QLabel("编程创造城市", self)
        lb1.move(100, 80)
        self.resize(500, 400)
        self.show()
        self.center()

    def center(self):
        dk = app.desktop()  # 获取屏幕
        self.move(dk.width()/2-self.width()/2, dk.height()/2-self.height()/2)    # 居中展示


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mf1 = MyForm1()
    sys.exit(app.exec_())
