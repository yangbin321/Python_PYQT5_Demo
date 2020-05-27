# -*- coding: utf-8 -*-

# @Author  : yangbin
# @Time    : 2020/5/25 16:28
# @File    : mainPy.py
# @desc    : 
import sys
from testDemo1.Designer.日历显示时间.日历显示时间 import Ui_Form
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtCore import QTime, QDate, QDateTime


# 想要使用这个类，就要载入这个类
class myClass(QWidget, Ui_Form):
    def __init__(self):
        super(myClass, self).__init__()
        self.initUI()

    def initUI(self):
        # 继承的实例化,这样可以载入已经定义好的界面
        self.setupUi(self)
        # 初始化设置一个时间
        self.timeEdit.setTime(QTime.fromString("12:12"))
        self.dateEdit.setDate(QDate.fromString("2020-01-01", "yyyy-MM-dd"))
        self.dateTimeEdit.setDateTime(QDateTime.fromString("2020-01-01 12:12", "yyyy-MM-dd HH:mm"))

        self.setWindowTitle("自定义显示现在时间")

        # 加载按钮点击事件信号槽
        self.btnReadNow.clicked.connect(self.btnReadNow_Click)

        # 日历选择事件
        self.calendar.selectionChanged.connect(self.calendar_Select)
        self.show()

    def btnReadNow_Click(self):
        # 获取当前时间
        dat = QDateTime.currentDateTime()
        # 将时间、日期、时间日期分别给设置
        self.timeEdit.setTime(dat.time())       # 时间
        self.dateEdit.setDate(dat.date())       # 日期
        self.dateTimeEdit.setDateTime(dat)      # 日期和时间

    def calendar_Select(self):
        date = self.calendar.selectedDate()
        print(date)
        self.lineEdit.setText(date.toString("yyyy年MM月dd日"))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mc = myClass()
    sys.exit(app.exec_())


