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

import re
import json
from urllib.request import urlopen
import requests

import json

base = "http://127.0.0.1:5000/"

gps_url = 'http://ipinfo.io/json'
response = urlopen(gps_url)
gps_data = json.load(response)

ip = gps_data['ip']
org = gps_data['org']
city = gps_data['city']
country = gps_data['country']
region = gps_data['region']
print('Ip: {0}, org: {1}, city: {2}, country: {3}, region: {4}'.format(ip,org,city,country,region))
list = []

class App(QStackedWidget):
    login_size = {
        "width":350,
        "height":200
    }
    main_size = {
        "width":350,
        "height":550
    }
    def resize(self,scene = "login_size"):
        if (scene == "login_size"):
            self.setFixedWidth(App.login_size["width"])
            self.setFixedHeight(App.login_size["height"])
        else:
            self.setFixedWidth(App.main_size["width"])
            self.setFixedHeight(App.main_size["height"])
    def __init__(self):
        super(App,self).__init__()
        login = LoginForm(self)
        main_window = MainWindow(self)
        self.addWidget(login)
        self.setWindowTitle("Location Sharing")
        self.addWidget(main_window)
        self.setFixedWidth(350)
        self.setFixedHeight(200)
        self.resize("login_size")
class LoginForm(QWidget):
    def __init__(self,manager= None):
        super(LoginForm,self).__init__()
        self.manager = manager
        uic.loadUi('login.ui',self)
        self.pushButton.clicked.connect(self.toMain)
        self.pushButton_3.clicked.connect(self.newLoginForm)
    def toMain(self):
        self.manager.setCurrentIndex(self.manager.currentIndex() + 1)
        self.manager.resize("main_size")
        #self.manager.currentWidget().label.setText("")
    def newLoginForm(self):
        new_window = App()
        list.append(new_window)
        new_window.show()

class MainWindow(QWidget):
    def __init__(self,manager= None):
        super(MainWindow,self).__init__()
        self.manager = manager
        uic.loadUi('mainwindow.ui',self)
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
        self.manager.resize("login_size")
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