#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author : yangbin
# @Time : 2020/5/24 13:36
# @File : 点击复选框弹出新窗口操作.py
# @Describe ：

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QCheckBox, QPushButton, QFrame, QMainWindow
from PyQt5.QtCore import Qt

class myClass(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("复选框QCheckBox")
        self.setGeometry(650, 300, 600, 500)
        myframe1 = QFrame(self)
        self.ck1 = QCheckBox("请点击我", myframe1)
        btn = QPushButton("退出", myframe1)
        btn.move(0, 100)
        # 信号与槽
        self.ck1.stateChanged[int].connect(self.myState)

        # 定义一个变量，用来存储关闭窗口的判断条件
        self.status = ""

        btn.clicked.connect(self.clickQuit)         # 主窗口的退出按钮
        myframe1.move(50, 50)
        self.show()

    # 点击退出的时候先关闭第二个窗口,再关闭第一个窗口
    def clickQuit(self):
        self.status = "close"       # 第二个窗口的关闭条件
        mc2.close()
        self.close()

    def myState(self, state):
        sText = self.sender()
        if state == Qt.Checked:
            # 打开新窗口
            self.status = "open"
            self.newWindonws()
        elif state == Qt.Unchecked:
            # 关闭新弹出来的窗口
            self.status = "close"
            mc2.close()

    # 打开新窗口的函数
    def newWindonws(self):
        mc2.show()

#第二个窗口的类
class myScendClass(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("第二个窗口")
        self.setGeometry(1100, 300, 500, 400)

    # 重写父类的关闭事件的方法
    def closeEvent(self, event):
        print("你点击了第二个窗口的关闭按钮")
        state = mc.status       # 获取复选框的状态
        if state == "open":
            event.ignore()
        else:
            event.accept()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mc = myClass()
    mc2 = myScendClass()
    sys.exit(app.exec_())

