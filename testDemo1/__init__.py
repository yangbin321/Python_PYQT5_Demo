#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author : yangbin
# @Time : 2020/5/22 17:13
# @File : 第一个PyQt5程序.py.py
# @Describe ：


import sys
from PyQt5.QtWidgets import QApplication, QWidget


class myClass(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mc = myClass()
    sys.exit(app.exec_())