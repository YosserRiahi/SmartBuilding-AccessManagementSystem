# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './login.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_FormLogin(object):
    def setupUi(self, FormLogin):
        FormLogin.setObjectName("FormLogin")
        FormLogin.resize(311, 210)
        FormLogin.setAutoFillBackground(False)
        FormLogin.setStyleSheet("background-color: rgb(40, 40, 40);")
        self.frame = QtWidgets.QFrame(FormLogin)
        self.frame.setGeometry(QtCore.QRect(20, 20, 271, 171))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.LE_login = QtWidgets.QLineEdit(self.frame)
        self.LE_login.setGeometry(QtCore.QRect(100, 10, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB")
        font.setBold(True)
        font.setWeight(75)
        self.LE_login.setFont(font)
        self.LE_login.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.LE_login.setObjectName("LE_login")
        self.LE_username = QtWidgets.QLabel(self.frame)
        self.LE_username.setGeometry(QtCore.QRect(10, 10, 61, 21))
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.LE_username.setFont(font)
        self.LE_username.setStyleSheet("color: rgb(255, 255, 255);")
        self.LE_username.setObjectName("LE_username")
        self.LE_password_2 = QtWidgets.QLabel(self.frame)
        self.LE_password_2.setGeometry(QtCore.QRect(10, 60, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.LE_password_2.setFont(font)
        self.LE_password_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.LE_password_2.setObjectName("LE_password_2")
        self.LE_password = QtWidgets.QLineEdit(self.frame)
        self.LE_password.setGeometry(QtCore.QRect(100, 60, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.LE_password.setFont(font)
        self.LE_password.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.LE_password.setObjectName("LE_password")
        self.BT_login = QtWidgets.QPushButton(self.frame)
        self.BT_login.setGeometry(QtCore.QRect(120, 110, 71, 61))
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.BT_login.setFont(font)
        self.BT_login.setStyleSheet("")
        self.BT_login.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/login.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.BT_login.setIcon(icon)
        self.BT_login.setIconSize(QtCore.QSize(50, 50))
        self.BT_login.setFlat(True)
        self.BT_login.setObjectName("BT_login")

        self.retranslateUi(FormLogin)
        QtCore.QMetaObject.connectSlotsByName(FormLogin)

    def retranslateUi(self, FormLogin):
        _translate = QtCore.QCoreApplication.translate
        FormLogin.setWindowTitle(_translate("FormLogin", " L O G I N"))
        self.LE_username.setText(_translate("FormLogin", "Username"))
        self.LE_password_2.setText(_translate("FormLogin", "Password"))


