import os
import subprocess
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox, QLineEdit
from GUI_login import Ui_FormLogin
from DatabaseAPI import CompanyDB

import sys


class main(QWidget, Ui_FormLogin):
    def __init__(self):
        QWidget.__init__(self)
        self.setupUi(self)
        self.BT_login.clicked.connect(self.login)
        self.LE_password.setEchoMode(QLineEdit.Password)

    def clearEntries(self):
        self.LE_login.clear()
        self.LE_password.clear()

    def login(self):
        db = CompanyDB()
        db.connectdDB()
        username = self.LE_login.text()
        password = self.LE_password.text()

        if(db.checkLogin(username, password)):
            print("login success")
            self.close()
            os.system("python W_dashboard.py")
        else:
            print("login failed")
            msgBox = QMessageBox()
            msgBox.setWindowTitle("Error")
            msgBox.setText("username or password is incorrect")
            msgBox.setIcon(QMessageBox.Critical)
            ret = msgBox.exec_()
        db.closeDB()
        self.clearEntries()

##----------------- Loop --------------------
app = QApplication(sys.argv)
window = main()
window.show()
app.exec()