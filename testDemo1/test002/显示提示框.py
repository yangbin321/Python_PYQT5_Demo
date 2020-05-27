#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author : yangbin
# @Time : 2020/5/22 21:07
# @File : 显示提示框.py
# @Describe ：

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QToolTip
from PyQt5.QtGui import QIcon, QFont


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = QWidget()
    w.setWindowTitle("显示提示框")
    w.setGeometry(600, 300, 800, 600)
    app.setWindowIcon(QIcon("./img/2.jpg"))
    # 设置提示字体的大小
    QToolTip.setFont(QFont("隶书", 20))
    w.setToolTip("显示提示框函数setToolTip")
    # 弄一个按钮的提示
    btn = QPushButton("点击我", w)
    btn.setToolTip("你点击我想干嘛啊？")
    btn.move(100, 80)
    w.show()
    sys.exit(app.exec_())

