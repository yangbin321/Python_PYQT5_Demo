# -*- coding: utf-8 -*-

# @Author  : yangbin
# @Time    : 2020/5/25 9:17
# @File    : init.py
# @desc    :

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QPixmap


class myClass(QWidget):
    def __init__(self):
        super().__init__()
        self.n = 1      # 全局变量
        self.timeOfPlay = 2000      # 定义轮播图的时间，单位为毫秒
        self.initUI()

    def initUI(self):
        self.setWindowTitle("轮播图")
        self.resize(500, 400)       # 设置窗口的大小

        # 图片的路径
        self.pm = QPixmap("./img/" + str(self.n) + ".jpg")
        self.imgLabel = QLabel(self)
        # 载入图片
        self.imgLabel.setPixmap(self.pm)
        # 设置图片的大小
        self.imgLabel.resize(300, 280)
        # 设置图片在窗体的位置
        self.imgLabel.move(self.width()/2-self.imgLabel.width()/2, self.height()/2-self.imgLabel.height()/2)
        # 设置图片自适应大小
        self.imgLabel.setScaledContents(True)

        # 设置图片轮播
        lunboLabel = QLabel(self)
        lunboLabel.setText("图片轮播")
        lunboLabel.move(self.width()/2-lunboLabel.width()/2 + 20, 20)

        # 定义一个掌握超时信号
        timer1 = QTimer(self)
        timer1.timeout.connect(self.timer_Timeout)
        # 设置超时的时间单位为毫秒
        timer1.start(self.timeOfPlay)

        self.show()

    # 定时轮播
    def timer_Timeout(self):
        print(self.n)
        # 图片每次加1
        self.n = self.n + 1
        if self.n > 7:
            self.n = 1
        # 重新设置图片的载入
        self.pm = QPixmap("./img/" + str(self.n) + ".jpg")
        # 重新加载图片
        self.imgLabel.setPixmap(self.pm)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mc = myClass()
    sys.exit(app.exec_())

