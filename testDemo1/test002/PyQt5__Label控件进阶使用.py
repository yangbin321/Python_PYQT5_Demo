# -*- coding: utf-8 -*-

# @Author  : yangbin
# @Time    : 2020/5/25 9:11
# @File    : PyQt5__Label控件进阶使用.py
# @desc    : 

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit


class myClass(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("PyQt5控件Label的进阶使用")
        self.resize(400, 300)
        # 名字的标签
        nameLabel = QLabel(self)
        nameLabel.setText("姓名（&1）：")
        nameLabel.move(90, 50)
        # 名字的编辑
        nameEdit = QLineEdit(self)
        nameEdit.move(165, 47)
        # 快捷键和输入框绑定
        nameLabel.setBuddy(nameEdit)

        # 愿望的标签
        dreamLabel = QLabel(self)
        dreamLabel.setText("愿望（&2）：")
        dreamLabel.move(90, 85)
        # 愿望的编辑
        dreamEdit = QLineEdit(self)
        dreamEdit.move(165, 82)
        # 快捷键和输入框绑定
        dreamLabel.setBuddy(dreamEdit)

        # 链接标签
        webLabel = QLabel(self)
        webLabel.setText("<a href='http://bcczcs.com'>编程创造城市</a>")
        # 设置允许打开外部链接的方式
        webLabel.setOpenExternalLinks(True)
        # 移动位置
        webLabel.move(190, 130)


        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mc = myClass()
    sys.exit(app.exec_())
