from PyQt5.QtCore import *
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox, QLineEdit
from GUI_zoneTime import Ui_FormZoneTime
from DatabaseAPI import CompanyDB, ZoneTime

import sys

class main(QWidget, Ui_FormZoneTime):
    def __init__(self):
        QWidget.__init__(self)
        self.setupUi(self)
        self.onCancel() #set intial times from database
        ##-------------------------- connect signals --------------------------
        self.BT_validate.clicked.connect(self.onValidate)
        self.BT_cancel.clicked.connect(self.onCancel)
        self.BT_home.clicked.connect(self.home)

    ##--------------------------  validate button clicked --------------------------
    def onValidate(self):
        zoneTime = ZoneTime() #instanciation from ZoneTime class

        zoneTime.zone1From = self.TE_zone1From.time().toString()
        zoneTime.zone1To = self.TE_zone1To.time().toString()
        zoneTime.zone2From = self.TE_zone2From.time().toString()
        zoneTime.zone2To = self.TE_zone2To.time().toString()
        zoneTime.zone3From = self.TE_zone3From.time().toString()
        zoneTime.zone3To = self.TE_zone3To.time().toString()

        db = CompanyDB()
        db.connectdDB()
        db.setTimeZoneAccess(zoneTime)
        db.closeDB()

        msgBox = QMessageBox()
        msgBox.setWindowTitle("Commit")
        msgBox.setText("Changes successfully added")
        msgBox.setIcon(QMessageBox.Information)
        ret = msgBox.exec_()

    ##--------------------------  cancel button clicked --------------------------
    def onCancel(self):
        zoneTime = ZoneTime()
        db = CompanyDB()
        db.connectdDB()
        zoneTime = db.getTimeZoneAccess()
        db.closeDB()

        self.TE_zone1From.setTime(QTime.fromString(zoneTime.zone1From))
        self.TE_zone1To.setTime(QTime.fromString(zoneTime.zone1To))
        self.TE_zone2From.setTime(QTime.fromString(zoneTime.zone2From))
        self.TE_zone2To.setTime(QTime.fromString(zoneTime.zone2To))
        self.TE_zone3From.setTime(QTime.fromString(zoneTime.zone3From))
        self.TE_zone3To.setTime(QTime.fromString(zoneTime.zone3To))

    ##--------------------------  home button clicked --------------------------
    def home(self):
        self.close() #close current form

##----------------- Loop --------------------
app = QApplication(sys.argv)
window = main()
window.show()
app.exec()