
from PyQt5.QtWidgets import QApplication, QWidget
from GUI_system import Ui_FormSystemControl

import sys


class main(QWidget, Ui_FormSystemControl):
    def __init__(self):
        QWidget.__init__(self)
        self.setupUi(self)
        ##-------------------------- connect signals --------------------------
        self.BT_AccessSysOFF.clicked.connect(self.onAccessSysOFF_Clicked)
        self.BT_AccessSysON.clicked.connect(self.onAccessSysON_Clicked)
        self.BT_SensorNotifOFF.clicked.connect(self.onSensorNotifOFF_Clicked)
        self.BT_SensorNotifON.clicked.connect(self.onSensorNotifON_Clicked)
        self.BT_home.clicked.connect(self.home)

        self.SL_accessSystem.valueChanged.connect(self.onAccessSysValueChanged)
        self.SL_sensorNotif.valueChanged.connect(self.onSensorNotifValueChanged)

    ##--------------------------  AccessSysOFF button clicked --------------------------
    def onAccessSysOFF_Clicked(self):
        print("onAccessSysOFF_Clicked")
        self.SL_accessSystem.setValue(0)


    ##--------------------------  AccessSysON button clicked --------------------------
    def onAccessSysON_Clicked(self):
        print("onAccessSysON_Clicked")
        self.SL_accessSystem.setValue(1)

    ##--------------------------  BensorNotifOFF button clicked --------------------------
    def onSensorNotifOFF_Clicked(self):
        print("onSensorNotifOFF_Clicked")
        self.SL_sensorNotif.setValue(0)

    ##--------------------------  SensorNotifON button clicked --------------------------
    def onSensorNotifON_Clicked(self):
        print("onBT_SensorNotifON_Clicked")
        self.SL_sensorNotif.setValue(1)


    ##--------------------------  AccessSys SlideBar value changed --------------------------
    def onAccessSysValueChanged(self):
        print("onAccessSysValueChanged")
        self.activateAcessSystem(self.SL_accessSystem.value())

    ##--------------------------  SensorNotif SlideBar value changed --------------------------
    def onSensorNotifValueChanged(self):
        print("onSensorNotifValueChanged")
        self.activateSensorNotif(self.SL_sensorNotif.value())


    ##--------------------------  activate/deactiavte Acess system --------------------------
    def activateAcessSystem(self, off_on):
        if(off_on):
            print("activate access system")
        else:
            print("deactivate access system")
    ##--------------------------  activate/deactiavte sensor notification --------------------------
    def activateSensorNotif(self, off_on):
        if(off_on):
            print("activate sensor notification")
        else:
            print("deactivate sensor notification")

    ##--------------------------  home button clicked --------------------------
    def home(self):
        self.close()  # close current form

##----------------- Loop --------------------
app = QApplication(sys.argv)
window = main()
window.show()
app.exec()