#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author : yangbin
# @Time : 2020/5/23 11:34
# @File : 按钮控件QPushButton.py
# @Describe ：

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QFrame, QVBoxLayout, QHBoxLayout
from PyQt5.QtGui import QColor


class myFrame(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("QPushButton的使用")
        dk = app.desktop()
        self.setGeometry(dk.width() / 2 - self.width() / 2, 300, 800, 500)

        # 设置一个全局变量的颜色为黑色
        self.color = QColor(0, 0, 0)

        # 设置三个按钮
        btnRead = QPushButton("红色")
        btnRead.setCheckable(True)          # 设置按钮的选中后的切换功能
        btnRead.clicked[bool].connect(self.setColor)            # 槽函数，并且判断是否有参数
        btnGreen = QPushButton("绿色")
        btnGreen.setCheckable(True)
        btnGreen.clicked[bool].connect(self.setColor)
        btnBlue = QPushButton("蓝色")
        btnBlue.setCheckable(True)
        btnBlue.clicked[bool].connect(self.setColor)
        # 设置一个纵向布局，并将三个按钮添加到这个布局中
        vblayout = QVBoxLayout()
        vblayout.addWidget(btnRead)
        vblayout.addWidget(btnGreen)
        vblayout.addWidget(btnBlue)
        # 设置一个QFrame，变成类的属性
        self.frame = QFrame()
        self.frame.setStyleSheet("QWidget{background-color:%s}" % self.color.name())       # 默认为黑色

        # 设置一个全局的横向布局，将vblayout和frame添加进去
        hbo = QHBoxLayout(self)
        hbo.addLayout(vblayout)     # 添加vblayout,是纵向的
        hbo.addWidget(self.frame)       #添加frame，是横向的

        self.show()

    # 设置颜色的改变
    def setColor(self, isPush):
        button = self.sender()
        # 根据是否选中按钮来觉得颜色的值是否拥有
        if isPush:
            v = 255
        else:
            v = 0
        # 根据按钮的文字来决定哪个参数被赋值为255或者0
        if button.text() == "红色":
            self.color.setRed(v)
        elif button.text() == "绿色":
            self.color.setGreen(v)
        elif button.text() == "蓝色":
            self.color.setBlue(v)
        # 设置好了以后，就赋值给右边的frame
        self.frame.setStyleSheet("QWidget{background-color:%s}" % self.color.name())
        # 输出颜色的名称
        print(self.color.name())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mf = myFrame()
    sys.exit(app.exec_())


