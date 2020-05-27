#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author : yangbin
# @Time : 2020/5/22 17:35
# @File : test003_python.py
# @Describe ：
import sys
from PyQt5.QtWidgets import QApplication, QWidget
sys.path.append("testDemo1")
from testDemo1.test001 import test003

if __name__ == '__main__':
    app = QApplication(sys.argv)        # 程序的初始化
    w = QWidget()
    mainWindows = test003.Ui_MainWindow()
    mainWindows.setupUi(w)
    w.show()
    sys.exit(app.exec_())       # 关闭程序的退出

