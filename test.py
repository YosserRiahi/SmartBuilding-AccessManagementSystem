# from DatabaseAPI import CompanyDB
#
# db = CompanyDB()
# db.connectdDB()
# data = db.selectEmp()
# #print (db.checkLogin('admin', '1234'))
#
# print (type(data[0][0]))
# import PyQt4

from datetime import date

from PyQt5.QtCore import *
from PyQt5.QtGui import *

from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox, QLineEdit, QTableWidgetItem, QDialog
from PyQt5.uic.properties import QtWidgets, QtGui, QtCore

from GUI_employee import Ui_Form


import sys


# class main(QWidget, Ui_Form):
#     ##---------------------  constructor ----------------------------
#     def __init__(self):
#         QWidget.__init__(self)
#         self.setupUi(self)
#
#
#
#
# ##----------------- Loop --------------------
# app = QApplication(sys.argv)
# window = main()
# window.show()
# app.exec()


import W_empHistory


from DatabaseAPI import  *

zoneTime = ZoneTime()
zoneTime.zone1From = '01:30:00'
zoneTime.zone1To = '20:00:00'
zoneTime.zone2From = '02:00:00'
zoneTime.zone2To = '16:00:00'
zoneTime.zone3From = '03:00:00'
zoneTime.zone3To = '17:00:00'

db = CompanyDB()
db.connectdDB()
table = db.getTimeZoneAccess()
db.closeDB()

print(table.zone1From)

