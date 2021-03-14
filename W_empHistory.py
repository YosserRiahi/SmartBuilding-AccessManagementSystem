from PyQt5.QtWidgets import QApplication, QWidget, QTableWidgetItem
from GUI_empHistory import Ui_FormEmpHist
from DatabaseAPI import CompanyDB

import sys



class main(QWidget, Ui_FormEmpHist):
    #------------ class atribute ----------------
    empID = int()
    currentZone = int()

    def __init__(self):
        QWidget.__init__(self)
        self.setupUi(self)
        self.setWindowTitle("  {} : {} {}".format(sys.argv[1], sys.argv[2], sys.argv[3]).upper())
        self.raise_()
        self.empID = sys.argv[1]
        self.T_EmpHisto.setColumnWidth(0, self.T_EmpHisto.width()/2) # resize header table with
        self.T_EmpHisto.setColumnWidth(1, self.T_EmpHisto.width()/2) # resize header table with
        self.showCurrentZone()
        self.updateEmpHistoTable()
        ##-------------------------- connect signals --------------------------
        # call updateEmpHistoTable() if any radioButton toogled
        self.RB_zone1.toggled.connect(self.updateEmpHistoTable)
        self.RB_zone2.toggled.connect(self.updateEmpHistoTable)
        self.RB_zone2.toggled.connect(self.updateEmpHistoTable)


        ##-------------------------------------------------------------------------

    ##--------- fill table of histo emp switch  selected zone by in radioButton -------------
    def updateEmpHistoTable(self):

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
        table = db.selectEmpHistory(zoneChecked, self.empID)
        db.closeDB()
        ##------------------------ fill table -----------------------------------

        if len(table):
            self.T_EmpHisto.setRowCount(len(table))
            self.T_EmpHisto.setColumnCount(len(table[0]))

            j = 0
            for row in table:
                for col in row:
                    self.T_EmpHisto.setItem(0, j, QTableWidgetItem(str(col)))
                    j += 1
        else:
            while self.T_EmpHisto.rowCount() > 0 :
                    self.T_EmpHisto.removeRow(0)

    ##--------- show employee current zone in Label(LB_currentZone) -------------
    def showCurrentZone(self):

        db = CompanyDB()
        db.connectdDB()
        zones = ('Outside', 'Zone 1', 'Zone 2', 'Zone 3')
        self.currentZone = db.getEmpCurrentZone(self.empID)
        self.LB_currentZone.setText(zones[self.currentZone]) #set label current zone
        db.closeDB()

##----------------- Loop --------------------
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = main()
    window.show()
    app.exec()