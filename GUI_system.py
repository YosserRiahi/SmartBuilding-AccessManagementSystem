# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './system.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_FormSystemControl(object):
    def setupUi(self, FormSystemControl):
        FormSystemControl.setObjectName("FormSystemControl")
        FormSystemControl.resize(530, 385)
        FormSystemControl.setStyleSheet("background-color:rgb(40, 40, 40)")
        self.BT_home = QtWidgets.QPushButton(FormSystemControl)
        self.BT_home.setGeometry(QtCore.QRect(450, 320, 75, 51))
        self.BT_home.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/home.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.BT_home.setIcon(icon)
        self.BT_home.setIconSize(QtCore.QSize(60, 60))
        self.BT_home.setFlat(True)
        self.BT_home.setObjectName("BT_home")
        self.BT_AccessSysOFF = QtWidgets.QPushButton(FormSystemControl)
        self.BT_AccessSysOFF.setGeometry(QtCore.QRect(60, 85, 71, 71))
        self.BT_AccessSysOFF.setStyleSheet("")
        self.BT_AccessSysOFF.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("img/cross-512.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.BT_AccessSysOFF.setIcon(icon1)
        self.BT_AccessSysOFF.setIconSize(QtCore.QSize(50, 50))
        self.BT_AccessSysOFF.setFlat(True)
        self.BT_AccessSysOFF.setObjectName("BT_AccessSysOFF")
        self.BT_AccessSysON = QtWidgets.QPushButton(FormSystemControl)
        self.BT_AccessSysON.setGeometry(QtCore.QRect(370, 90, 61, 61))
        self.BT_AccessSysON.setStyleSheet("")
        self.BT_AccessSysON.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("img/validate.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.BT_AccessSysON.setIcon(icon2)
        self.BT_AccessSysON.setIconSize(QtCore.QSize(80, 80))
        self.BT_AccessSysON.setFlat(True)
        self.BT_AccessSysON.setObjectName("BT_AccessSysON")
        self.label = QtWidgets.QLabel(FormSystemControl)
        self.label.setGeometry(QtCore.QRect(180, 65, 161, 16))
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color:white;")
        self.label.setObjectName("label")
        self.SL_accessSystem = QtWidgets.QSlider(FormSystemControl)
        self.SL_accessSystem.setGeometry(QtCore.QRect(150, 110, 201, 22))
        self.SL_accessSystem.setMaximum(1)
        self.SL_accessSystem.setPageStep(0)
        self.SL_accessSystem.setOrientation(QtCore.Qt.Horizontal)
        self.SL_accessSystem.setObjectName("SL_accessSystem")
        self.BT_SensorNotifOFF = QtWidgets.QPushButton(FormSystemControl)
        self.BT_SensorNotifOFF.setGeometry(QtCore.QRect(60, 185, 71, 71))
        self.BT_SensorNotifOFF.setStyleSheet("")
        self.BT_SensorNotifOFF.setText("")
        self.BT_SensorNotifOFF.setIcon(icon1)
        self.BT_SensorNotifOFF.setIconSize(QtCore.QSize(50, 50))
        self.BT_SensorNotifOFF.setFlat(True)
        self.BT_SensorNotifOFF.setObjectName("BT_SensorNotifOFF")
        self.BT_SensorNotifON = QtWidgets.QPushButton(FormSystemControl)
        self.BT_SensorNotifON.setGeometry(QtCore.QRect(370, 190, 61, 61))
        self.BT_SensorNotifON.setStyleSheet("")
        self.BT_SensorNotifON.setText("")
        self.BT_SensorNotifON.setIcon(icon2)
        self.BT_SensorNotifON.setIconSize(QtCore.QSize(80, 80))
        self.BT_SensorNotifON.setFlat(True)
        self.BT_SensorNotifON.setObjectName("BT_SensorNotifON")
        self.label_2 = QtWidgets.QLabel(FormSystemControl)
        self.label_2.setGeometry(QtCore.QRect(190, 170, 161, 16))
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color:white;")
        self.label_2.setObjectName("label_2")
        self.SL_sensorNotif = QtWidgets.QSlider(FormSystemControl)
        self.SL_sensorNotif.setGeometry(QtCore.QRect(150, 210, 201, 22))
        self.SL_sensorNotif.setMaximum(1)
        self.SL_sensorNotif.setPageStep(0)
        self.SL_sensorNotif.setOrientation(QtCore.Qt.Horizontal)
        self.SL_sensorNotif.setObjectName("SL_sensorNotif")

        self.retranslateUi(FormSystemControl)
        QtCore.QMetaObject.connectSlotsByName(FormSystemControl)

    def retranslateUi(self, FormSystemControl):
        _translate = QtCore.QCoreApplication.translate
        FormSystemControl.setWindowTitle(_translate("FormSystemControl", "    S Y S T E M     C O N T R O L"))
        self.label.setText(_translate("FormSystemControl", "        Acees system"))
        self.label_2.setText(_translate("FormSystemControl", "Sensor notification"))

