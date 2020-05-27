#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author : yangbin
# @Time : 2020/5/24 9:47
# @File : 进度条QProgressbar.py
# @Describe ：

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QProgressBar, QVBoxLayout, QHBoxLayout, QPushButton
from PyQt5.QtCore import QBasicTimer        # 时钟控件


class myClass(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("进度条QProgressBar")
        self.setGeometry(700, 300, 500, 400)
        self.lab = QLabel("进度条", self)
        self.lab.move(45, 50)
        # 进度条控件
        self.qgb = QProgressBar(self)
        self.qgb.move(100, 50)
        # 控件的大小
        self.qgb.resize(300, 20)
        # 配置一个值，控制进度条时钟,表示当前进度
        self.pv = 0
        # 声明一个时钟控件
        self.timerl = QBasicTimer()

        # 设置最大值和最小值
        self.qgb.setMinimum(0)
        self.qgb.setMaximum(100)
        # 设置当前进度
        self.qgb.setValue(self.pv)

        # 载入按钮
        self.btn = QPushButton("开始", self)
        self.btn.move(100, 80)
        self.btn.clicked.connect(self.myTimeChange)     # 信号

        self.show()

    # 时钟控件切换的核心代码
    def myTimeChange(self):
        # 判断控件是否已经开启
        if self.timerl.isActive():
            self.timerl.stop()
            self.btn.setText("开始")
        else:
            self.timerl.start(100, self)        # 每隔一秒
            self.btn.setText("停止")

    # 重写时间控件的方法
    def timerEvent(self, e):
        if self.pv == 100:
            self.timerl.stop()
            self.btn.setText("完成")
            self.btn.clicked.connect(self.close)        # 点击完成后退出
            print("完成")
        else:
            self.pv = self.pv + 1
            self.qgb.setValue(self.pv)
            print(self.pv)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mc = myClass()
    sys.exit(app.exec_())
