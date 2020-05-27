#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author : yangbin
# @Time : 2020/5/23 10:01
# @File : 相对布局.py
# @Describe ：

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QGridLayout, QLineEdit, QLabel, QPushButton


class MyBuJuClass(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("相对布局")
        self.setGeometry(app.desktop().width()/2 - self.width()/2, app.desktop().height()/2 - self.height()/2, 600, 400)

        # QLineEdit只能编辑单行的文本框,QLabel标签
        labelCode = QLabel("验证码", self)
        leCode = QLineEdit(self)
        btnCode = QPushButton("提交", self)

        # 定义一个水平方向布局，没有添加窗体
        hlayout = QHBoxLayout()
        # 将控件添加到水平布局上
        hlayout.addWidget(labelCode)
        hlayout.addWidget(leCode)
        hlayout.addWidget(btnCode)
        # 增加一个弹簧，让后面都留空，显得布局更加好看
        hlayout.addStretch()
        # 垂直布局，self是最外层的窗体
        vlayout = QVBoxLayout(self)
        # 将水平布局添加搭配垂直布局
        vlayout.addLayout(hlayout)
        vlayout.addStretch()
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    myBJ = MyBuJuClass()
    sys.exit(app.exec_())

