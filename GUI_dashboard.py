# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './dashboard.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_FormDashbord(object):
    def setupUi(self, FormDashbord):
        FormDashbord.setObjectName("FormDashbord")
        FormDashbord.resize(1024, 699)
        FormDashbord.setStyleSheet("background-color:rgb(60, 60, 60)")
        self.BT_employees = QtWidgets.QPushButton(FormDashbord)
        self.BT_employees.setGeometry(QtCore.QRect(10, 10, 497, 335))
        self.BT_employees.setStyleSheet("background-color: rgb(40, 40, 40);\n"
"")
        self.BT_employees.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/employees.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.BT_employees.setIcon(icon)
        self.BT_employees.setIconSize(QtCore.QSize(220, 220))
        self.BT_employees.setObjectName("BT_employees")
        self.BT_history = QtWidgets.QPushButton(FormDashbord)
        self.BT_history.setGeometry(QtCore.QRect(517, 10, 497, 335))
        self.BT_history.setStyleSheet("background-color:rgb(40, 40, 40);")
        self.BT_history.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("img/history.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.BT_history.setIcon(icon1)
        self.BT_history.setIconSize(QtCore.QSize(180, 180))
        self.BT_history.setObjectName("BT_history")
        self.BT_timezone = QtWidgets.QPushButton(FormDashbord)
        self.BT_timezone.setGeometry(QtCore.QRect(10, 355, 497, 335))
        self.BT_timezone.setStyleSheet("background-color:rgb(40, 40, 40);")
        self.BT_timezone.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("img/acces2.gif"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.BT_timezone.setIcon(icon2)
        self.BT_timezone.setIconSize(QtCore.QSize(200, 200))
        self.BT_timezone.setObjectName("BT_timezone")
        self.BT_system = QtWidgets.QPushButton(FormDashbord)
        self.BT_system.setGeometry(QtCore.QRect(517, 355, 497, 335))
        self.BT_system.setStyleSheet("background-color:rgb(40, 40, 40);")
        self.BT_system.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("img/connection.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.BT_system.setIcon(icon3)
        self.BT_system.setIconSize(QtCore.QSize(220, 220))
        self.BT_system.setObjectName("BT_system")

        self.retranslateUi(FormDashbord)
        QtCore.QMetaObject.connectSlotsByName(FormDashbord)

    def retranslateUi(self, FormDashbord):
        _translate = QtCore.QCoreApplication.translate
        FormDashbord.setWindowTitle(_translate("FormDashbord", "       D A S H B O A R D"))


