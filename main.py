# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import sys
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QApplication, QWidget,QDialog
from PyQt5 import uic
from PyQt5 import QtCore
from PyQt5 import QtWidgets
from PyQt5 import QtGui

from PyQt5.QtWidgets import QStackedWidget
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QMessageBox
import re
import json
from urllib.request import urlopen
import requests
from city import a

import json
print(len(a))
base = "http://127.0.0.1:5000/"

# gps_url = 'http://ipinfo.io/json'
# response = urlopen(gps_url)
# gps_data = json.load(response)
#
# ip = gps_data['ip']
# org = gps_data['org']
# city = gps_data['city']
# country = gps_data['country']
# region = gps_data['region']
# print('Ip: {0}, org: {1}, city: {2}, country: {3}, region: {4}'.format(ip,org,city,country,region))


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
    signup_size = {
        "width": 450,
        "height": 250
    }
    def resize(self,scene = "login_size"):
        if (scene == "login_size"):
            self.setFixedWidth(App.login_size["width"])
            self.setFixedHeight(App.login_size["height"])
        elif (scene == "main_size"):
            self.setFixedWidth(App.main_size["width"])
            self.setFixedHeight(App.main_size["height"])
        else:
            self.setFixedWidth(App.signup_size["width"])
            self.setFixedHeight(App.signup_size["height"])
    def __init__(self):
        super(App,self).__init__()
        self.login = LoginForm(self)
        self.main_window = MainWindow(self)
        self.addWidget(self.login)
        self.setWindowTitle("Location Sharing")
        self.addWidget(self.main_window)
        self.signup_size = SignUpForm(self)
        self.addWidget(self.signup_size)
        self.user  = {"userName":"huydang2k3","fullName":"Huy Dang", "age":"21","gender": "Male","password":"123",
                      "avatarUrl":"", "counter":"","currentCityName":""}
        self.resize("login_size")
    #clear neighbor list
    def clear_data(self):
        self.main_window.clear_data()
class SignUpForm(QWidget):
    def __init__(self,manager= None):
        super(SignUpForm,self).__init__()
        self.manager = manager
        uic.loadUi('SignUp.ui',self)
        self.pushButton.clicked.connect(self.signUp)
        self.pushButton_3.clicked.connect(self.toLogin)
    def signUp(self):
        #call sign up api
        result = False
        if (result):
            msg = QMessageBox()
            msg.setWindowTitle("Sign Up Successfully")
            msg.setText("Now you can get started")
            msg.exec_()
            self.toLogin()
            # self.manager.currentWidget().label.setText("")
        else:
            msg = QMessageBox()
            msg.setWindowTitle("Sign Fail")
            msg.setText("Username existed. Please choose another")
            msg.exec_()
    def toLogin(self):
        self.manager.setCurrentIndex(self.manager.currentIndex() - 2)
        self.manager.resize("login_size")


class LoginForm(QWidget):
    def __init__(self,manager= None):
        super(LoginForm,self).__init__()
        self.manager = manager
        uic.loadUi('login.ui',self)
        self.pushButton.clicked.connect(self.login)
        self.pushButton_3.clicked.connect(self.newLoginForm)
        self.pushButton_2.clicked.connect(self.toSignUp)
    def toMain(self,user):
        self.manager.setCurrentIndex(self.manager.currentIndex() + 1)
        self.manager.main_window.gen_personal_data(user)
        self.manager.resize("main_size")
    def login(self):
        #call login api
        # self.user = request.get...
        result = True
        if (result):

            self.toMain(self.manager.user)
        else:
            msg = QMessageBox()
            msg.setWindowTitle("Login Fail")
            msg.setText("Wrong user name or password")
            msg.exec_()
    def toSignUp(self):
        self.manager.setCurrentIndex(self.manager.currentIndex() + 2)
        self.manager.resize("signup_size")
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

        self.comboBox.view().pressed.connect(self.on_choose)
        #province select dropdown
        for i in range(64):
            self.comboBox.addItem("")
        _translate = QtCore.QCoreApplication.translate
        for i in range(64):
            self.comboBox.setItemText(i, _translate("Form", a[i]["province"]))

        self.lay = QVBoxLayout()
        self.scrollAreaWidgetContents.setLayout(self.lay)
        self.lay.setSpacing(10)
        # t = QHBoxLayout()
        # img = QLabel(self)
        # pixmap = QPixmap('ava.png')
        # img.setPixmap(pixmap)
        # t.addWidget(img)
        # self.scrollArea.widget().children().insert(2,t)
        # self.scrollArea.widget().children().insert(3,t)
        # self.scrollArea.widget().children().insert(4,t)
        # self.scrollArea.widget().children().insert(5,t)
    def on_choose(self,index):
        location = self.comboBox.model().itemFromIndex(index).text()
        #call api with location
        print(location)
    def gen_personal_data(self,user):
        #calculate age from date of birth
        # ...
        self.label.setText(user['fullName'])
        self.label_3.setText(user['gender'])
        self.label_6.setText('21')
        self.label_4.setText(user['userName'])
    def clear_data(self):
        for i in reversed(range(self.lay.count())):
            self.lay.itemAt(i).widget().setParent(None)
    def toLogin(self):

        self.manager.setCurrentIndex(self.manager.currentIndex() - 1)
        self.manager.resize("login_size")
        self.clear_data()
    def search(self):
        self.clear_data()
        # response = requests.get(base + 'h')
        users = [{"fullName":"Huy Dang", "age":"21","gender": "Male"},
                 {"fullName":"Son Mai", "age":"21","gender": "Male"},
                 {"fullName":"Duong Dao", "age":"21","gender": "Gay"}
                 ]
        # users = [{"fullName": "Huy Dang", "age": "21", "gender": "Male"},
        #          {"fullName": "Son Mai", "age": "21", "gender": "Male"}
        #          ]
        # create a user box
        for u in users:

            horizontalLayoutWidget = QtWidgets.QWidget()
            #horizontalLayoutWidget.setGeometry(QtCore.QRect(220, 20, 160, 54))
            horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
            horizontalLayout = QtWidgets.QHBoxLayout(horizontalLayoutWidget)
            horizontalLayout.setContentsMargins(0, 0, 0, 0)
            horizontalLayout.setObjectName("horizontalLayout")
            horizontalLayoutWidget.setSizePolicy(QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed));
            self.lay.addWidget(horizontalLayoutWidget)
            # ava
            label = QtWidgets.QLabel(horizontalLayoutWidget)
            label.setText("")
            label.setPixmap(QtGui.QPixmap("ava.png"))
            label.setObjectName("label")
            horizontalLayout.addWidget(label)

            # inforbox
            verticalLayout = QtWidgets.QVBoxLayout()
            verticalLayout.setObjectName("verticalLayout")
            horizontalLayout.addLayout(verticalLayout)

            # name
            label_2 = QtWidgets.QLabel(horizontalLayoutWidget)
            label_2.setObjectName("label_2")
            label_2.setText(u['fullName'])
            verticalLayout.addWidget(label_2)
            # age
            label_3 = QtWidgets.QLabel(horizontalLayoutWidget)
            label_3.setObjectName("label_3")
            label_3.setText(u['gender']+', '+ u["age"])
            verticalLayout.addWidget(label_3)
app = QApplication(sys.argv)
widgets = App()
list.append(widgets)
widgets.show()

def func():
    #call update locate api
    print('hi')
import threading

def set_interval(func, sec):
    def func_wrapper():
        set_interval(func, sec)
        func()
    t = threading.Timer(sec, func_wrapper)
    t.start()
    return t
set_interval(func,3600)
try:
    sys.exit(app.exec_())
except:
    print('Closing')
