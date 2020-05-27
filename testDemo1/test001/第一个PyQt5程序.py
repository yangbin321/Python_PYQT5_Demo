#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author : yangbin
# @Time : 2020/5/22 17:13
# @File : 第一个PyQt5程序.py.py
# @Describe ：

import sys
from PyQt5.QtWidgets import QApplication, QWidget

if __name__ == '__main__':
    app = QApplication(sys.argv)        # 程序的初始化
    window = QWidget()      # 新建立一个窗口
    window.resize(500, 400)     # 设置窗口的大小
    window.setWindowTitle("第一个pyqt5程序")     # 设置标题
    window.move(700, 300)       # 出现的位置
    window.show()       # 窗口的显示
    sys.exit(app.exec_())       # 关闭程序的退出

