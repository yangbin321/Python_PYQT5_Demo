#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author : yangbin
# @Time : 2020/5/24 10:44
# @File : 下拉列表控件QComboBox.py
# @Describe ：
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QComboBox, QFrame


class myClass(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("下拉列表控件QComboBox")
        self.setGeometry(700, 300, 600, 500)

        myframe1 = QFrame(self)
        myframe1.move(50, 50)
        lbl_1 = QLabel("省", myframe1)
        lbl_1.move(0, 3)
        comBox1 = QComboBox(myframe1)
        comBox1.move(30, 0)

        # 传递字符串类型
        comBox1.activated[str].connect(self.myActived)      # 选择以后可以进行信号处理
        # 省份
        comBox1.addItem("选择省份")
        comBox1.addItem("广西")
        comBox1.addItem("广东")
        comBox1.addItem("福建")
        comBox1.addItem("北京")

        # 市级
        lbl_2 = QLabel("市", myframe1)
        lbl_2.move(170, 3)
        self.comBox2 = QComboBox(myframe1)
        self.comBox2.move(200, 0)
        self.comBox2.activated[str].connect(self.myActived2)

        self.show()

    def myActived(self, strName):
        # 每次选择之前先清空
        self.comBox2.clear()
        print(strName)
        if strName == "广西":
            self.comBox2.addItem("南宁")
            self.comBox2.addItem("贵港")
            self.comBox2.addItem("柳州")
            self.comBox2.addItem("桂林")
            self.comBox2.addItem("玉林")
            self.comBox2.addItem("防城港")
            self.comBox2.addItem("平果")
        elif strName == "广东":
            self.comBox2.addItem("广州")
            self.comBox2.addItem("深圳")
            self.comBox2.addItem("东莞")
            self.comBox2.addItem("珠海")
            self.comBox2.addItem("中山")
            self.comBox2.addItem("佛山")
            self.comBox2.addItem("惠州")
        elif strName == "福建":
            self.comBox2.addItem("厦门")
            self.comBox2.addItem("泉州")
        elif strName == "北京":
            self.comBox2.addItem("朝阳")
            self.comBox2.addItem("一环")
            self.comBox2.addItem("二环")
        elif strName == "选择省份":
            self.comBox2.clear()

    def myActived2(self, strName):
        print(strName)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mc = myClass()
    sys.exit(app.exec_())
