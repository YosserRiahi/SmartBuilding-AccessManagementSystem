import subprocess
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from PyQt5.QtWidgets import QApplication, QWidget, QTableWidgetItem

from GUI_employee import Ui_Form
from DatabaseAPI import CompanyDB, Employee

import sys


class main(QWidget, Ui_Form):
    ##---------------------  constructor ----------------------------
    def __init__(self):
        QWidget.__init__(self)
        self.setupUi(self)

        ##--------------------- design Calendar ----------------------------
        charFormatWeekend = QTextCharFormat()
        charFormatWeekend.setForeground(QBrush(QColor(192, 255, 133), Qt.SolidPattern))
        self.CAL_startdate.setWeekdayTextFormat(Qt.Saturday, charFormatWeekend)
        self.CAL_startdate.setWeekdayTextFormat(Qt.Sunday, charFormatWeekend)

        charFormatHeader = QTextCharFormat()
        charFormatHeader.setForeground((QBrush(Qt.white, Qt.SolidPattern)))
        charFormatHeader.setBackground((QBrush(QColor(240, 136, 17), Qt.SolidPattern)))

        self.CAL_startdate.setHeaderTextFormat(charFormatHeader)
        #-------------------------- connect signals --------------------------
        self.T_employeeInfo.itemSelectionChanged.connect(self.onTableSelectedChanged)
        self.T_employeeInfo.doubleClicked.connect(self.onTableDoubleClick)
        self.LE_search.textChanged.connect(self.fillTableEmp)
        self.BT_add.clicked.connect(self.addEmp)
        self.BT_edit.clicked.connect(self.editEmp)
        self.BT_delete.clicked.connect(self.deleteEmp)
        self.BT_clear.clicked.connect(self.emptyEntries)
        self.BT_home.clicked.connect(self.home)

        ##-------------------------------------------------------------------------
        self.fillTableEmp()

    ## -------------------------- fill Table employee --------------------------
    def fillTableEmp(self):
        db = CompanyDB()
        db.connectdDB()

        st = self.LE_search.text()
        if len(st):
            querry = '''select * from employees where ( ID like '%{}%' or NAME like '%{}%' or LASTNAME like '%{}%')'''.format(st, st , st)
            table = db.selectFiltEmp(querry)
        else:
            table = db.selectEmp()
        # -----------------fill tablle ---------------
        try:
            self.T_employeeInfo.setRowCount(len(table))
            self.T_employeeInfo.setColumnCount(len(table[0]))

            j = 0
            for row in table:
                for col in row:
                    self.T_employeeInfo.setItem(0, j, QTableWidgetItem(str(col)))
                    j += 1
        except:
            pass
        #---------------------------------------------------------
        db.closeDB()

    ## -------------------------- empty entries ans comboBoxes --------------------------
    def emptyEntries(self):
        entries = (self.LE_ID, self.LE_name, self.LE_lastname, self.LE_position, self.LE_pin, self.LE_tag,
                   self.LE_tag, self.LE_finger)

        for entry in entries:
            entry.clear()

        comboBoxes = (self.CB_z1, self.CB_z2, self.CB_z3)

        for comboBoxe in comboBoxes:
            comboBoxe.setChecked(False)

    ## -------------------------- entries to employee  object--------------------------
    def entriesToEmpObj(self):
        empl = Employee()
        empl.id = int(self.LE_ID.text())
        empl.name = self.LE_name.text()
        empl.lastname = self.LE_lastname.text()
        empl.position = self.LE_position.text()
        empl.pin = self.LE_pin.text()
        empl.tag = self.LE_tag.text()
        empl.finger = self.LE_finger.text()
        empl.privilege = int(self.CB_z1.isChecked())+ 2* int(self.CB_z2.isChecked()) + 4* int(self.CB_z3.isChecked())
        empl.startDate = (self.CAL_startdate.selectedDate()).toString('yyyy-MM-dd')
        return empl

    ## -------------------------- save Employee info to database--------------------------
    def addEmp(self):
        try:
            db = CompanyDB()
            db.connectdDB()
            db.insertEmp(self.entriesToEmpObj())
            db.closeDB()
            self.fillTableEmp()
            self.emptyEntries()
        except:
            pass
    ## -------------------------- edit Employee --------------------------
    def editEmp(self):
        try:
            currentSelected = (self.T_employeeInfo.selectionModel().selectedRows())[0].row()
            selectedID = int(self.T_employeeInfo.item(currentSelected, 0).text())

            db = CompanyDB()
            db.connectdDB()
            db.editEmp(self.entriesToEmpObj(), selectedID)
            db.closeDB()
            self.fillTableEmp()
            self.emptyEntries()
        except:
            pass

    ## -------------------------- edit Employee --------------------------
    def deleteEmp(self):
        try:
            currentSelected = (self.T_employeeInfo.selectionModel().selectedRows())[0].row()
            selectedID = int(self.T_employeeInfo.item(currentSelected, 0).text())

            db = CompanyDB()
            db.connectdDB()
            db.delEmp(selectedID)
            db.closeDB()
            self.fillTableEmp()
            self.emptyEntries()
        except:
            pass

    ##--------------------------- Table selection changed -----------------
    def onTableSelectedChanged(self):
        try:
            selectedRows = self.T_employeeInfo.selectionModel().selectedRows()
            currentSelected = selectedRows[0].row()
            print(self.T_employeeInfo.item(currentSelected,0).text())
            self.LE_ID.setText(self.T_employeeInfo.item(currentSelected,0).text())
            self.LE_name.setText(self.T_employeeInfo.item(currentSelected,1).text())
            self.LE_lastname.setText(self.T_employeeInfo.item(currentSelected,2).text())
            self.LE_position.setText(self.T_employeeInfo.item(currentSelected,3).text())
            self.LE_pin.setText(self.T_employeeInfo.item(currentSelected,5).text())
            self.LE_tag.setText( self.T_employeeInfo.item(currentSelected,6).text())
            self.LE_finger.setText(self.T_employeeInfo.item(currentSelected,7).text())

            privilege = int(self.T_employeeInfo.item(currentSelected,8).text())
            self.CB_z1.setChecked(bool(privilege&1))
            self.CB_z2.setChecked(bool((privilege>>1)&1))
            self.CB_z3.setChecked(bool((privilege>>2)&1))

            date = self.T_employeeInfo.item(currentSelected,4).text()
            qDate = QDate(int(date.split('-')[0]), int(date.split('-')[1]), int(date.split('-')[2]));

            self.CAL_startdate.setSelectedDate(qDate)

        except:
            pass

    ##--------------------------- Table double row click -----------------
    def onTableDoubleClick(self):
        try:
            currentSelected = (self.T_employeeInfo.selectionModel().selectedRows())[0].row()
            selectedID = int(self.T_employeeInfo.item(currentSelected, 0).text())
            selectedName = self.T_employeeInfo.item(currentSelected, 1).text()
            selectedLastName = self.T_employeeInfo.item(currentSelected, 2).text()
            subprocess.Popen("python W_empHistory.py {} {} {}".format(selectedID, selectedName, selectedLastName))

        except Exception as ex:
            print("EXCEPTION")
            print(ex)

    ##--------------------------  home button clicked --------------------------
    def home(self):
        self.close()  # close current form

##----------------- Loop --------------------
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = main()
    window.show()
    app.exec()



