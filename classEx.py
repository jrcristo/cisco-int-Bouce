import funtions_jose


class AccessPoint:
    def __init__(self, apName, ipaddress, wlcIp):
        self.apName = apName
        self.ipAddress = ipaddress
        self.wlcIp = wlcIp

    def getWlcIp(self, var):
        return self.wlcIp + var

    def associateWithWlc(self):
        pass

    def shutNoshut(self):
        pass

    def printApDetails(self):
        print(self.apName, self.ipAddress)


class Wlc:
    def __init__(self, wlcIp, username, password):
        self.ip = wlcIp
        self.username = username
        self.password = password
        self.connectedAps = []


    def attachAp(self, accessPoint):
        if accessPoint not in self.connectedAps:
            self.connectedAps.append(accessPoint)

    def showApList(self):
        for ap in self.connectedAps:
            ap.printApDetails()


apFirstFloor = AccessPoint("apFirstFloor", "10.10.10.10", "12.12.12.12")

apJC = funtions_jose.connect_wlc(True)
wlc = Wlc(apJC['ip'], apJC["username"], apJC["password"])
wlc.attachAp(apFirstFloor)


wlc.showApList()
