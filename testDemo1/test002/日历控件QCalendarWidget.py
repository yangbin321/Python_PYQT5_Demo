#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author : yangbin
# @Time : 2020/5/24 11:25
# @File : 日历控件QCalendarWidget.py
# @Describe ：

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QCalendarWidget, QLabel, QVBoxLayout
from PyQt5.QtGui import QFont
from PyQt5.QtCore import QDate


# 实现一个日历控件
class myClass(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("日历控件QCalendarWidget.py")
        self.setGeometry(700, 300, 600, 500)

        cal = QCalendarWidget()
        cal.clicked[QDate].connect(self.myCalend)
        self.lbel = QLabel("这里显示日期")
        self.lbel.setFont(QFont("华文行楷", 20))

        # 盒子模型
        vlo = QVBoxLayout(self)
        vlo.addWidget(cal)
        vlo.addWidget(self.lbel)

        self.show()

    def myCalend(self, date):
        mydte = QDate(date)         # 重写时间
        self.lbel.setText(mydte.toString("yyyy-MM-dd"))
        print(mydte.toString("yyyy-MM-dd"))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mc = myClass()
    sys.exit(app.exec_())
