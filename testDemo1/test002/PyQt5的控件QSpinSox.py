# -*- coding: utf-8 -*-

# @Author  : yangbin
# @Time    : 2020/5/25 9:17
# @File    : init.py
# @desc    :

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QSpinBox, QDoubleSpinBox
from PyQt5.QtCore import Qt


class myClass(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("PyQt5的控件QSpinSox")
        self.resize(300, 200)

        # 设置布局
        hvol = QHBoxLayout(self)
        # QSpinBox
        qsb = QSpinBox(self)
        # 设置可以取数的范围
        qsb.setRange(0, 20)
        # 设置前缀
        qsb.setPrefix("物品 ")
        # 设置后缀
        qsb.setSuffix(" 件")

        # 添加到水平布局中
        hvol.addWidget(qsb)

        # 价格
        qdsp = QDoubleSpinBox(self)
        qdsp.setRange(0, 100000000)
        qdsp.setPrefix("价格 ")
        qdsp.setSuffix(" 元")
        # 设置增加的步长
        qdsp.setSingleStep(0.5)
        # 添加到水平布局中
        hvol.addWidget(qdsp)


        # 设置水平布局的控件位于最上方
        hvol.setAlignment(Qt.AlignTop)


        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mc = myClass()
    sys.exit(app.exec_())

