# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './zoneHisto.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_FormHistoZone(object):
    def setupUi(self, FormHistoZone):
        FormHistoZone.setObjectName("FormHistoZone")
        FormHistoZone.resize(1024, 612)
        FormHistoZone.setStyleSheet("background-color:rgb(40, 40, 40)")
        self.T_histoZone = QtWidgets.QTableWidget(FormHistoZone)
        self.T_histoZone.setGeometry(QtCore.QRect(30, 60, 971, 451))
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB")
        font.setPointSize(10)
        self.T_histoZone.setFont(font)
        self.T_histoZone.setStyleSheet("color:white;")
        self.T_histoZone.setObjectName("T_histoZone")
        self.T_histoZone.setColumnCount(5)
        self.T_histoZone.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setForeground(brush)
        self.T_histoZone.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setForeground(brush)
        self.T_histoZone.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setForeground(brush)
        self.T_histoZone.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setForeground(brush)
        self.T_histoZone.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setForeground(brush)
        self.T_histoZone.setHorizontalHeaderItem(4, item)
        self.widget = QtWidgets.QWidget(FormHistoZone)
        self.widget.setGeometry(QtCore.QRect(230, 0, 671, 41))
        self.widget.setObjectName("widget")
        self.RB_zone1 = QtWidgets.QRadioButton(self.widget)
        self.RB_zone1.setGeometry(QtCore.QRect(30, 20, 91, 17))
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.RB_zone1.setFont(font)
        self.RB_zone1.setStyleSheet("color:rgb(255, 255, 255)")
        self.RB_zone1.setChecked(True)
        self.RB_zone1.setObjectName("RB_zone1")
        self.RB_zone2 = QtWidgets.QRadioButton(self.widget)
        self.RB_zone2.setGeometry(QtCore.QRect(240, 20, 91, 17))
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.RB_zone2.setFont(font)
        self.RB_zone2.setStyleSheet("color:rgb(255, 255, 255)")
        self.RB_zone2.setObjectName("RB_zone2")
        self.RB_zone3 = QtWidgets.QRadioButton(self.widget)
        self.RB_zone3.setGeometry(QtCore.QRect(460, 20, 91, 17))
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.RB_zone3.setFont(font)
        self.RB_zone3.setStyleSheet("color:rgb(255, 255, 255)")
        self.RB_zone3.setObjectName("RB_zone3")
        self.BT_home = QtWidgets.QPushButton(FormHistoZone)
        self.BT_home.setGeometry(QtCore.QRect(920, 530, 75, 51))
        self.BT_home.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/home.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.BT_home.setIcon(icon)
        self.BT_home.setIconSize(QtCore.QSize(60, 60))
        self.BT_home.setFlat(True)
        self.BT_home.setObjectName("BT_home")

        self.retranslateUi(FormHistoZone)
        QtCore.QMetaObject.connectSlotsByName(FormHistoZone)

    def retranslateUi(self, FormHistoZone):
        _translate = QtCore.QCoreApplication.translate
        FormHistoZone.setWindowTitle(_translate("FormHistoZone", "   Z O N E     H I S T O R Y"))
        item = self.T_histoZone.horizontalHeaderItem(0)
        item.setText(_translate("FormHistoZone", "Log ID"))
        item = self.T_histoZone.horizontalHeaderItem(1)
        item.setText(_translate("FormHistoZone", "ID"))
        item = self.T_histoZone.horizontalHeaderItem(2)
        item.setText(_translate("FormHistoZone", "Date in"))
        item = self.T_histoZone.horizontalHeaderItem(3)
        item.setText(_translate("FormHistoZone", "Date out"))
        item = self.T_histoZone.horizontalHeaderItem(4)
        item.setText(_translate("FormHistoZone", "state"))
        self.RB_zone1.setText(_translate("FormHistoZone", "Zone 1"))
        self.RB_zone2.setText(_translate("FormHistoZone", "Zone 2"))
        self.RB_zone3.setText(_translate("FormHistoZone", "Zone 3"))


