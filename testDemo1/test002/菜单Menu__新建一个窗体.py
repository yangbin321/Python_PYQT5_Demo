#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author : yangbin
# @Time : 2020/5/24 12:38
# @File : 菜单Menu__新建一个窗体.py
# @Describe ：

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QMenu, QMessageBox, QAction


class myClass(QMainWindow):     # 继承QMainWindow
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("菜单Menu")
        self.setGeometry(700, 300, 600, 500)
        # 开始制作菜单
        # 利用窗体本身有的菜单栏功能进行载入
        myMenu = self.menuBar()         # 菜单栏的返回对象
        fileMenu = myMenu.addMenu("文件")

        # 新建窗体的功能
        actNewWindows = QAction("新建窗体", self)
        actNewWindows.triggered.connect(self.myNewWindows)      # 槽
        fileMenu.addAction(actNewWindows)

        # 新二级子菜单
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
        self.setGeometry(800, 300, 600, 500)

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
