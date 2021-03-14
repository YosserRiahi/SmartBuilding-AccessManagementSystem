import os
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox, QLineEdit, QTableWidgetItem, QDialog
from GUI_dashboard import Ui_FormDashbord
import sys

class main(QWidget, Ui_FormDashbord):
    ##---------------------  constructor ----------------------------
    def __init__(self):
        QWidget.__init__(self)
        self.setupUi(self)
        ##-------------------------- connect signals --------------------------
        self.BT_employees.clicked.connect(self.openEmployeeForm)
        self.BT_history.clicked.connect(self.openHistoryForm)
        self.BT_timezone.clicked.connect(self.openTimezoneForm)
        self.BT_system.clicked.connect(self.openSystemForm)

    ##------------------ open employee form ------------------------
    def openEmployeeForm(self):
        self.hide()
        os.system("python W_employee.py") #waitting until form closed
        self.show()

    ##------------------ open history form ------------------------
    def openHistoryForm(self):
        self.hide()
        os.system("python W_zoneHisto.py")
        self.show()

    ##------------------ open timezone form ------------------------
    def openTimezoneForm(self):
        self.hide()
        os.system("python W_zoneTime.py")
        self.show()

    ##------------------ open system form ------------------------
    def openSystemForm(self):
        self.hide()
        os.system("python W_system.py")
        self.show()

##----------------- Loop --------------------
app = QApplication(sys.argv)
window = main()
window.show()
app.exec()
