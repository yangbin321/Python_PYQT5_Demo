#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author : yangbin
# @Time : 2020/5/22 21:36
# @File : pyqt5类封装.py
# @Describe ：

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton


class myClass(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("类封装程序")
        self.resize(800, 600)
        btn = QPushButton("点击我退出", self)
        btn.move(100, 100)
        btn.clicked.connect(self.close)     # 退出按钮
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mc = myClass()
    sys.exit(app.exec_())


