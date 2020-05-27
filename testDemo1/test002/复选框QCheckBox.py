#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author : yangbin
# @Time : 2020/5/23 13:30
# @File : 复选框QCheckBox.py
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
        self.ck1 = QCheckBox("唱歌", myframe1)
        self.ck2 = QCheckBox("跳舞", myframe1)
        btn = QPushButton("退出", myframe1)
        self.ck2.move(0, 50)
        btn.move(0, 100)

        self.ck1.stateChanged[int].connect(self.myState)
        self.ck2.stateChanged[int].connect(self.myState)

        btn.clicked.connect(self.close)         # 退出按钮
        myframe1.move(50, 50)
        self.show()

    def myState(self, state):
        sText = self.sender()
        if state == Qt.Checked:
            print(state, "选中", sText.text())
        elif state == Qt.Unchecked:
            print(state, "未选中", sText.text())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mc = myClass()
    sys.exit(app.exec_())

