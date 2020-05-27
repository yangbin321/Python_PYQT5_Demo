#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author : yangbin
# @Time : 2020/5/22 20:52
# @File : 设置窗体图标.py
# @Describe ：

import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = QWidget()
    w.setWindowTitle("这是一个设置窗口标题的程序——1")      # 标题
    w.setWindowIcon(QIcon("img/头像.jpg"))        # 设置图标
    w.show()

    w2 = QWidget()
    w2.setWindowTitle("这是一个设置窗口标题的程序——2")  # 标题
    w2.setWindowIcon(QIcon("img/2.jpg"))  # 设置图标
    w2.show()
    sys.exit(app.exec_())
