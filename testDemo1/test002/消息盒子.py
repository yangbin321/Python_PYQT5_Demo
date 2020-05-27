#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author : yangbin
# @Time : 2020/5/22 22:05
# @File : 消息盒子.py
# @Describe ：

import sys
from PyQt5.QtWidgets import QMessageBox, QApplication, QWidget, QPushButton


class myMessageClass(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(800, 400, 400, 300)
        self.setWindowTitle("消息盒子")
        btn = QPushButton("关闭窗体", self)
        btn.move(100, 50)
        # 点击关闭按钮的时候，执行的是窗体的关闭，等同于点击窗体右上角的自带窗体的X按钮的效果
        btn.clicked.connect(self.close)
        self.show()

    # 重写父类的关闭事件的方法
    def closeEvent(self, event):
        print("你点击了关闭窗体的按钮")
        # question(加载的控件，标题，内容，消息的类型选择方式（yes no），默认方式)。结果返回是一个按钮的结果
        result = QMessageBox.question(self, "杨小彬提示您：", "您真的要关闭窗体了吗？", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if result == QMessageBox.Yes:
            print("关闭")
            print(dir(event))
            event.accept()
        else:
            print("取消")
            event.ignore()
            # QMessageBox.information(self, "消息", "谢谢你不关闭我！")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mc = myMessageClass()
    sys.exit(app.exec_())

