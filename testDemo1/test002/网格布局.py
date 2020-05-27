#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author : yangbin
# @Time : 2020/5/23 10:32
# @File : 网格布局.py
# @Describe ：

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QTextEdit, \
    QLineEdit, QLabel, QHBoxLayout, QVBoxLayout, QPushButton
from PyQt5.QtGui import QFont


class myBuJuClass(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("网格布局")
        self.setGeometry(700, 300, 600, 500)

        # 设置一个简单的网格布局
        labelTitle = QLabel("标题")
        labelTitle.setFont(QFont('宋体', 14))
        labelAuthor = QLabel("作者")
        labelAuthor.setFont(QFont('宋体', 14))
        labelContent = QLabel("内容")
        labelContent.setFont(QFont('宋体', 14))
        btn = QPushButton("提交")
        btn.setFont(QFont('宋体', 14))

        # 编辑的单行文本框
        leTitle = QLineEdit()
        leAuthor = QLineEdit()
        leContent = QTextEdit()

        # 设置一个网格布局,窗体为最外层的窗体
        gridl = QGridLayout(self)
        # 将每个控件分隔开一定的空间距离
        gridl.setSpacing(20)
        # 将标签和文本框一个一个添加进去，
        gridl.addWidget(labelTitle, 0, 0)   # 第1行的第1列
        gridl.addWidget(leTitle, 0, 1)   # 第1行的第2列

        gridl.addWidget(labelAuthor, 1, 0)   # 第2行的第1列
        gridl.addWidget(leAuthor, 1, 1)   # 第2行的第2列

        gridl.addWidget(labelContent, 2, 0)   # 第3行的第1列
        gridl.addWidget(leContent, 2, 1)   # 第3行的第2列
        gridl.addWidget(btn, 3, 1)      # 提交按钮

        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mw = myBuJuClass()
    sys.exit(app.exec_())



