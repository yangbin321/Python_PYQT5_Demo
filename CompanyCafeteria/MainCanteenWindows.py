#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author : yangbin
# @Time : 2020/5/24 12:38
# @File : 菜单Menu__新建一个窗体.py
# @Describe ：

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QMenu, QMessageBox, QAction, QLabel, QPushButton, QFrame
from PyQt5.QtGui import QIcon, QFont, QPixmap
from PyQt5.QtCore import Qt


class myClass(QMainWindow):     # 继承QMainWindow
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("中移在线广西分公司—食堂金额结算主界面")
        self.setWindowIcon(QIcon("./img/canteen.png"))
        self.resize(540, 720)
        # 开始制作菜单，利用窗体本身有的菜单栏功能进行载入
        # 菜单栏的返回对象
        myMenu = self.menuBar()
        # 在菜单栏添加第一个菜单“文件”
        fileMenu = myMenu.addMenu("文件")
        # 文件中添加一个新建窗口的功能，并设置触发事件
        actNewWindows = QAction("新建窗口", self)
        actNewWindows.triggered.connect(self.myNewWindows)      # 信号与槽
        fileMenu.addAction(actNewWindows)

        """设置标签，用来存放拍照的载体"""

        """ 设置拍照的按钮和字体大小"""
        self.btnTakePicture = QPushButton("拍    照", self)
        # 设置按钮的大小
        self.btnTakePicture.resize(110, 45)
        btnTakePicture_Font = QFont()
        btnTakePicture_Font.setFamily("微软雅黑")  # 设置字体的种类
        btnTakePicture_Font.setPointSize(15)  # 设置字体的大小
        btnTakePicture_Font.setBold(True)  # 设置字体为粗体
        # btnSettleAccounts_Font.setWeight(20)
        # 设置按钮的字体大小
        self.btnTakePicture.setFont(btnTakePicture_Font)
        # 设置按钮在界面的位置
        self.btnTakePicture.move(30, 620)

        """ 设置金额结算按钮和字体大小"""
        self.btnSettleAccounts = QPushButton("金额结算", self)
        # 设置按钮的大小
        self.btnSettleAccounts.resize(110, 45)
        btnSettleAccounts_Font = QFont()
        btnSettleAccounts_Font.setFamily("微软雅黑")        # 设置字体的种类
        btnSettleAccounts_Font.setPointSize(15)     # 设置字体的大小
        btnSettleAccounts_Font.setBold(True)        # 设置字体为粗体
        # btnSettleAccounts_Font.setWeight(20)
        # 设置按钮的字体大小
        self.btnSettleAccounts.setFont(btnSettleAccounts_Font)
        # 设置按钮在界面的位置
        self.btnSettleAccounts.move(400, 620)

        """新二级子菜单"""
        child1 = fileMenu.addMenu("文件1")
        child1.addAction("学习")
        child1.addAction("工作")
        child2 = fileMenu.addMenu("文件2")
        child2.addAction("唱歌")
        child2.addAction("跳舞")
        child3 = fileMenu.addMenu("文件3")
        child3.addAction("吃饭")
        child3.addAction("睡觉")

        # 菜单栏的其他按钮
        myMenu.addAction("运行")
        myMenu.addAction("编辑")
        myMenu.addAction("查看")
        actHelp = QAction("帮助", self)     # 赋值给最大的窗体
        actHelp.triggered.connect(self.myHelp)          # 行为触发的事件，利用QAction中的触发triggered,赋值给槽myHelp
        myMenu.addAction(actHelp)

        # 主窗口的显示
        self.show()

    def myHelp(self):
        msgBox = QMessageBox(QMessageBox.Information, "帮助提示", "内容：欢迎加杨彬微信3838438交流！", QMessageBox.Ok, self)
        msgBox.show()       # 记得要显示

    # 新建窗口的方法
    def myNewWindows(self):
        mc2.show()      # 仅仅这样调用，只能产生一个窗口

# 第二个窗体的类
class myScendClass(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("新建窗口")
        self.setWindowIcon(QIcon("./img/canteen.png"))
        self.resize(540, 720)
        self.move(950, 60)

        """
            如果定义了全局变量后，在这里调用self.show()，会同时弹出，
            在哪里调用新窗口，就在哪里调用，如本例在:
                def myNewWindows(self):
                    mc2.show()
        """


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mc = myClass()
    mc2 = myScendClass()
    sys.exit(app.exec_())
