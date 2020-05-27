#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author : yangbin
# @Time : 2020/5/23 13:08
# @File : 单行文本框QLineEdit.py
# @Describe ：
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QLabel


class myClass(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("单行文本框QLineEdit")
        self.setGeometry(400, 200, 800, 600)
        self.lable1 = QLabel("显示区", self)
        self.lable1.move(50, 50)

        le = QLineEdit(self)
        le.textChanged[str].connect(self.ybText)
        self.show()

    def ybText(self, str):
        self.lable1.setText(str)
        self.lable1.adjustSize()
        print(str)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mc = myClass()
    sys.exit(app.exec_())
