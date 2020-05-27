#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author : yangbin
# @Time : 2020/5/24 17:26
# @File : 登录窗体实战.py
# @Describe ：

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox, QLabel, QLineEdit, QPushButton, QFrame
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import Qt


class myClass(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("用户登录界面")
        dk = app.desktop()
        self.setGeometry(dk.width()/2 -self.width()/2, 300, 350, 250)
        self.setWindowIcon(QIcon("./img/用户.png"))

        myframe1 = QFrame(self)
        myframe1.setGeometry(0, 0, 250, 200)

        label1 = QLabel("用户名：", myframe1)
        label1.setFont(QFont("微软雅黑", 10))
        label2 = QLabel("密   码：", myframe1)
        label2.setFont(QFont("微软雅黑", 10))
        label1.move(5, 10)
        label2.move(5, 50)

        self.lineUsername = QLineEdit(myframe1)
        self.linePassword = QLineEdit(myframe1)
        self.lineUsername.move(70, 11)
        self.linePassword.move(70, 50)
        # 设置密码不可见
        self.linePassword.setEchoMode(QLineEdit.Password)

        # 设置按钮
        btnLogin = QPushButton("登录", myframe1)
        btnQuit = QPushButton("退出", myframe1)
        btnLogin.move(20, 90)
        btnQuit.move(130, 90)

        # 登录和退出的操作
        btnLogin.clicked.connect(self.myButtonClick)
        btnQuit.clicked.connect(self.myButtonClick)

        # 隐藏窗口右上角的缩小放大的按钮
        self.setWindowFlags(Qt.WindowCloseButtonHint)

        self.show()

    def myButtonClick(self):
        source = self.sender()
        if source.text() == "登录":
            print("登录")
            QMessageBox.information(self, "用户信息", "用户名：" + self.lineUsername.text() + "，密码：" + self.linePassword.text(), QMessageBox.Ok)
        elif source.text() == "退出":
            # 退出
            print("退出")
            QApplication.instance().exit()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mc = myClass()
    sys.exit(app.exec_())

