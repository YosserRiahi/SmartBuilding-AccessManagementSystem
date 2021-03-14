from PyQt5.QtWidgets import QApplication, QWidget,  QTableWidgetItem
from GUI_zoneHisto import Ui_FormHistoZone
from DatabaseAPI import CompanyDB

import sys


class main(QWidget, Ui_FormHistoZone):
    ##---------------------  constructor ----------------------------
    def __init__(self):
        QWidget.__init__(self)
        self.setupUi(self)
        ##-------------------------- connect signals --------------------------
        # call updateEmpHistoTable() if any radioButton toogled
        self.RB_zone1.toggled.connect(self.updateTableHisto)
        self.RB_zone2.toggled.connect(self.updateTableHisto)
        self.RB_zone2.toggled.connect(self.updateTableHisto)

        self.BT_home.clicked.connect(self.home)
        ##------------------- # resize header table width --------------
        self.T_histoZone.setColumnWidth(0, self.T_histoZone.width()/5)
        self.T_histoZone.setColumnWidth(1, self.T_histoZone.width()/5)
        self.T_histoZone.setColumnWidth(2, self.T_histoZone.width()/5)
        self.T_histoZone.setColumnWidth(3, self.T_histoZone.width()/5)
        self.T_histoZone.setColumnWidth(4, self.T_histoZone.width()/5)

        self.updateTableHisto()

    def updateTableHisto(self):
        ##---------------------- get which radioButton is checked ---------------------------
        zoneChecked = int()
        if self.RB_zone1.isChecked():
            zoneChecked = 1
        elif self.RB_zone2.isChecked():
            zoneChecked = 2
        elif self.RB_zone3.isChecked():
            zoneChecked = 3
         ##------------------- get table from Database ---------------------------
        db = CompanyDB()
        db.connectdDB()
        table = db.selectHistZone(zoneChecked)
        db.closeDB()
        ##------------------------ fill table -----------------------------------

        if len(table):
            self.T_histoZone.setRowCount(len(table))
            self.T_histoZone.setColumnCount(len(table[0]))

            j = 0
            for row in table:
                for col in row:
                    self.T_histoZone.setItem(0, j, QTableWidgetItem(str(col)))
                    j += 1
        else:
            while self.T_histoZone.rowCount() > 0 :
                    self.T_histoZone.removeRow(0)

    ##--------------------------  home button clicked --------------------------
    def home(self):
        self.close()  # close current form

##----------------- Loop --------------------
app = QApplication(sys.argv)
window = main()
window.show()
app.exec()