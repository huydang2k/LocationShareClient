# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import sys
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QApplication, QWidget,QDialog
from PyQt5 import uic
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QStackedWidget

import requests

import json

base = "http://127.0.0.1:5000/"


list = []

class App(QStackedWidget):
    def __init__(self):
        super(App,self).__init__()
        login = LoginForm(self)
        main_window = MainWindow(self)
        self.addWidget(login)
        self.setWindowTitle("Location Sharing")
        self.addWidget(main_window)
        self.setFixedWidth(350)
        self.setFixedHeight(500)

class LoginForm(QWidget):
    def __init__(self,manager= None):
        super(LoginForm,self).__init__()
        self.manager = manager
        uic.loadUi('login.ui',self)
        self.pushButton.clicked.connect(self.toMain)
        self.pushButton_3.clicked.connect(self.newLoginForm)
    def toMain(self):
        self.manager.setCurrentIndex(self.manager.currentIndex() + 1)
        #self.manager.currentWidget().label.setText("")
    def newLoginForm(self):
        new_window = App()
        list.append(new_window)
        new_window.show()

class MainWindow(QWidget):
    def __init__(self,manager= None):
        super(MainWindow,self).__init__()
        self.manager = manager
        uic.loadUi('ui2.ui',self)
        self.pushButton_2.clicked.connect(self.toLogin)
        self.pushButton.clicked.connect(self.search)
        # t = QHBoxLayout()
        # img = QLabel(self)
        # pixmap = QPixmap('ava.png')
        # img.setPixmap(pixmap)
        # t.addWidget(img)
        # self.scrollArea.widget().children().insert(2,t)
        # self.scrollArea.widget().children().insert(3,t)
        # self.scrollArea.widget().children().insert(4,t)
        # self.scrollArea.widget().children().insert(5,t)


        print(self.scrollAreaWidgetContents)
    def toLogin(self):
        self.manager.setCurrentIndex(self.manager.currentIndex() - 1)
    def search(self):
        return
        # response = requests.get(base + 'h')
        # self.label.setText(dict(response.json())["data"])
app = QApplication(sys.argv)
widgets = App()
list.append(widgets)
widgets.show()

try:
    sys.exit(app.exec_())
except:
    print('Closing')