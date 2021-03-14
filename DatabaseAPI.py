import pymysql
from datetime import datetime


## class Employee
class Employee:
    id = int()
    name = str()
    lastname = str()
    position = str()
    startDate = str()
    pin = str()
    tag = str()
    finger = str()
    privilege = int

## class ZoneTime
class ZoneTime:
    zone1From = None
    zone2From = None
    zone3From = None
    zone1To = None
    zone2To = None
    zone3To = None

class CompanyDB:
    connection = None
## --------------------------connect to DB--------------------------
    def connectdDB(self):
        self.connection =  pymysql.connect(host="localhost", user="root", database="company")

## --------------------------connect to DB--------------------------
    def closeDB(self):
        self.connection.close()

## --------------------------insert new employee--------------------------
    def insertEmp(self,emp):
        cur = self.connection.cursor()
        cur.execute('''INSERT INTO `employees`(`ID`, `NAME`, `LASTNAME`, `POSITION`, `START_DATE`, `PIN`, `TAG`,`FINGER`, `PRIVILEGE`)
                    VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s )''',
                    (emp.id, emp.name, emp.lastname, emp.position, emp.startDate, emp.pin, emp.tag, emp.finger, emp.privilege))
        self.connection.commit()

    ## -------------------------- edit employee--------------------------
    def editEmp(self, emp, selectedID):
        cur = self.connection.cursor()
        cur.execute('''UPDATE `employees` SET `ID`= %s,`NAME`= %s ,`LASTNAME`= %s ,`POSITION`= %s ,`START_DATE`= %s ,`PIN`= %s ,
        `TAG`= %s,`FINGER`= %s,`PRIVILEGE`= %s  WHERE `ID`= %s ''',
                    (emp.id, emp.name, emp.lastname, emp.position, emp.startDate, emp.pin, emp.tag, emp.finger,
                     emp.privilege, selectedID))
        self.connection.commit()

    ## -------------------------- delete employee--------------------------
    def delEmp(self, selectedID):
        cur = self.connection.cursor()
        cur.execute('''DELETE FROM `employees` WHERE ID = %s ''',[selectedID])
        self.connection.commit()

#     ## --------------------------edit pin code--------------------------
#     def editPin(self, id, pin):
#         cur = self.connection.cursor()
#         cur.execute('''UPDATE `employees` SET `PIN`= %s WHERE `ID`=%s''',(pin, id))
#         self.connection.commit()
#
# ## --------------------------edit tag--------------------------
#     def editTag(self,id, tag):
#         cur = self.connection.cursor()
#         cur.execute('''UPDATE `employees` SET `TAG`= %s WHERE `ID`=%s''',(tag, id))
#         self.connection.commit()

## --------------------------get employrees table--------------------------
    def selectEmp(self):
        cur = self.connection.cursor()
        cur.execute('''SELECT * FROM `employees''')
        table = cur.fetchall()
        ## affichage ##
        print ("----------+-+----------+-+----------+-+----------+-+----------+-+----------+-+----------+-+----------+-+----------+-+")
        print ("{:^10}|||{:^10}|||{:^10}|||{:^10}|||{:^10}|||{:^10}|||{:^10}|||{:^10}|||{:^10}|||".format(
                                                'id', 'name', 'lastname', 'position', 'startDate','pin', 'tag', 'finger', 'privilege'))
        print ("----------+-+----------+-+----------+-+----------+-+----------+-+----------+-+----------+-+----------+-+----------+-+")

        for row in table:
            print ("{:^10}|||{:^10}|||{:^10}|||{:^10}|||{:^10}|||{:^10}|||{:^10}|||{:^10}|||{:^10}|||".format(
                                                            row[0], row[1],row[2], row[3], str(row[4]), row[5], row[6], row[7], row[8]))
            print ("----------+-+----------+-+----------+-+----------+-+----------+-+----------+-+----------+-+----------+-+----------+-+")
        return table

    #  --------------------------get filtered employrees table--------------------------
    def selectFiltEmp(self, filterQuerry):
        cur = self.connection.cursor()
        cur.execute(filterQuerry)
        table = cur.fetchall()
        return table

    ## -------------------------- get employree History by zone --------------------------
    def selectEmpHistory(self, zone, id):
        cur = self.connection.cursor()
        cur.execute('''SELECT DATE_IN, DATE_OUT FROM `histo_zone%s` where ID = %s''',(zone, id))
        table = cur.fetchall()
        return table
    ## -------------------------- get employree current Zone --------------------------
    def getEmpCurrentZone(self, id):
        currentZone = int()
        cur = self.connection.cursor()
        for zone in range(3,0,-1): # range(3,0,-1) return [3, 2, 1]
            cur.execute('''SELECT `STATE` from histo_zone%s where `STATE`=1 and ID = %s''',(zone, id))
            try:
                currentZone = int(cur.fetchall()[0][0])
                if currentZone:
                    currentZone = zone
                return currentZone
            except :
                return 0

    ## --------------------------check employee by PIN--------------------------
    def checkEmpPin(self, id, pin):
        cur = self.connection.cursor()
        cur.execute('''SELECT * from employees WHERE ID = %s and PIN = %s''',(id, pin))

        if not (len(cur.fetchall())) :
            print ("PIN OR ID IS INCORRECT")
            return 0 ## wrong PIN or ID
        else:
            return id

## --------------------------check employee by tag--------------------------
    def checkEmpTag(self, tag):
        cur = self.connection.cursor()
        cur.execute('''SELECT ID from employees WHERE tag = %s''',[tag])

        try:
            ID = int(cur.fetchall()[0][0])
        except :
            print ("TAG NOT FOUND")
            ID = 0 ## wrong tag
        return ID

## --------------------------check employee by Finger--------------------------
    def checkEmpFinger(self, finger):
        cur = self.connection.cursor()
        cur.execute('''SELECT ID from employees WHERE finger = %s''', [finger])

        try:
            ID = int(cur.fetchall()[0][0])
        except:
            print ("FINGERPRINT NOT FOUND")
            ID = 0  ## wrong tag
        return ID

## --------------------------check employee by tag--------------------------
    def getPrevilege(self, id, zone):
        cur = self.connection.cursor()
        cur.execute('''SELECT `PRIVILEGE` FROM `employees`WHERE `ID` = %s''',[id])

        try:
            PREVILEGE = int(cur.fetchall()[0][0])
        except :
            PREVILEGE = 0

        print ("PREVILEGE employee N{} = {}".format(id, PREVILEGE))

        return (PREVILEGE >> (zone-1)) & 1


## --------------------------check employee by tag--------------------------
    def checkTimeInterval(self, zone):
        cur = self.connection.cursor()
        cur.execute('''SELECT `MIN_TIME`, `MAX_TIME` FROM `zone_config` WHERE `ZONE` = %s''',[zone])

        minTime, maxTime = (cur.fetchall()[0])
        minTime = int(str(minTime).split(':')[0])
        maxTime = int(str(maxTime).split(':')[0])

        if datetime.now().hour >= minTime and datetime.now().hour< maxTime:
            print("ZONE{} is allowed now".format(zone))
            return True
        else:
            print("ZONE{} is not allowed now".format(zone))
            return False

## --------------------------IN employee (pointage a l'entree)--------------------------
    def inEmp(self, id, zone):
        cur = self.connection.cursor()
        cur.execute('''INSERT INTO `histo_zone%s`(`ID`) VALUES (%s)''',(zone, id))
        self.connection.commit()

## --------------------------OUT employee (pointage a la sortie)--------------------------
    def outEmp(self, id, zone):
        cur = self.connection.cursor()
        cur.execute('''UPDATE `histo_zone%s` SET `DATE_OUT`=CURRENT_TIMESTAMP(),`STATE`=2 WHERE `ID` = %s and `STATE` = 1''', (zone, id))
        self.connection.commit()

## --------------------------employee attendence--------------------------
    def checkEmpState(self, id, zone):

        # STATE = 1 -> employee inside
        # STATE = 2 -> employee left

        cur = self.connection.cursor()
        cur.execute('''SELECT STATE FROM histo_zone%s where STATE = 1 and ID = %s''',(zone, id))

        try:
            ID = int(cur.fetchall()[0][0])
        except :
            ID = 0
        return ID

## --------------------------get history table--------------------------
    def selectHistZone(self, zone):
        cur = self.connection.cursor()
        cur.execute('''SELECT * FROM `histo_zone%s`''',[zone])
        table = cur.fetchall()
        print ("----------+-+----------+-+--------------------+-+--------------------+-+----------+-+")
        print ("{:^10}|||{:^10}|||{:^20}|||{:^20}|||{:^10}|||".format('Log_ID', 'ID', 'DATE_IN', 'DATE_OUT', 'STATE'))
        print ("----------+-+----------+-+--------------------+-+--------------------+-+----------+-+")

        for row in table :
            print ("{:^10}|||{:^10}|||{:^20}|||{:^20}|||{:^10}|||".format(row[0], row[1], str(row[2]), str(row[3]), row[4]))
            print ("----------+-+----------+-+--------------------+-+--------------------+-+----------+-+")
        return table
    ##--------------------------check login--------------------------
    def checkLogin(self, username, password):
        cur = self.connection.cursor()
        cur.execute('''SELECT `username`FROM `login` WHERE `username`=%s and `password`= %s''',(username, password))
        result = bool()
        try:
            cur.fetchall()[0][0] #return exception for null result
            result = True
            print("password is correct")
        except :
            result = False
            print("password is incorrect")
        return result

    ##-------------------------- set Time Zone Access --------------------------
    def setTimeZoneAccess(self, zoneTime):

        cur = self.connection.cursor()

        # use "executemany" instead of "execute" to execute multiple query
        cur.executemany('''UPDATE `zone_config` SET `MIN_TIME`=%s,`MAX_TIME`=%s WHERE `ZONE`=%s''',
                          [(zoneTime.zone1From, zoneTime.zone1To, 1),(zoneTime.zone2From, zoneTime.zone2To, 2),
                         (zoneTime.zone3From, zoneTime.zone3To, 3)])
        self.connection.commit()

    ##-------------------------- set Time Zone Access --------------------------
    def getTimeZoneAccess(self):
        zoneTime = ZoneTime()
        cur = self.connection.cursor()
        cur.execute('''SELECT `MIN_TIME`, `MAX_TIME` FROM `zone_config`''')
        table = cur.fetchall()
        zoneTime.zone1From = self.convertDBTimeToString(str(table[0][0]))
        zoneTime.zone1To = self.convertDBTimeToString(str(table[0][1]))
        zoneTime.zone2From = self.convertDBTimeToString(str(table[1][0]))
        zoneTime.zone2To = self.convertDBTimeToString(str(table[1][1]))
        zoneTime.zone3From = self.convertDBTimeToString(str(table[2][0]))
        zoneTime.zone3To = self.convertDBTimeToString(str(table[2][1]))
        return zoneTime

    ##-------------------------- convert Database time to string  --------------------------
    def convertDBTimeToString(self, dbTime): #exemple "2:30:00" --> "02:30:00"
        hour = int(dbTime.split(':')[0])
        minute = int(dbTime.split(':')[1])
        return "{:02d}:{:02d}:00".format(hour, minute)
