#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author : yangbin
# @Time : 2020/5/24 9:16
# @File : 滑块QSlider.py
# @Describe ：

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QSlider, QLabel, QHBoxLayout, QVBoxLayout, QToolTip
from PyQt5.QtGui import QColor
from PyQt5.QtCore import Qt

class myClass(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("滑块QSliser")
        self.setGeometry(500, 300, 500, 400)
        qlabel = QLabel("进度条", self)
        qslider = QSlider(Qt.Horizontal, self)          # 设置水平方向的滑块Qt.Horizontal，也可以设置为1
        qslider.setMaximum(255)         # 滑块的最大值
        qslider.setMinimum(0)           # # 滑块的最小值设置
        qslider.valueChanged[int].connect(self.myValue)
        hlayout = QHBoxLayout()         # 水平方向布局
        hlayout.addWidget(qlabel)       # 添加容器
        hlayout.addWidget(qslider)      # 添加容器
        # hlayout.addStretch()
        vol = QVBoxLayout(self)         # 垂直方向布局
        vol.addLayout(hlayout)
        vol.addStretch()                # 弹簧压缩
        qslider.setStyleSheet("QWidget{background:balck}")       # 滑块初始化的颜色
        self.show()

    def myValue(self, num):
        print(num)
        mycolor = QColor(0, 0, 0)
        mycolor.setRed(num)
        self.setStyleSheet("QWidget{background:%s}" % mycolor.name())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mc = myClass()
    sys.exit(app.exec_())
