from DistanceData import *
# This is a simple class that creates a truck object
class Truck():
    def __init__(self, ID):
        self.ID = ID

    def truckLoadPackages(self, distance, address, packageList, truck):
        truckPackages = ['','','','','','','','','','','','','','','','']
        packageQue = []
        for j in range(40):
            packageQue.append(packageList.search(j+1))
        i = 0
        lastAddress = 'HUB'
        while i < len(truckPackages):
            packageValid = False
            minDistance = minDistanceFrom(distance, address, lastAddress, packageQue)
            for package in packageQue:
                if package.address == minDistance:
                    if truck == 2:
                        if package.ID == 3 or 18 or 36 or 38: # this is not working
                            packageValid = True
                    packageValid = True
                    if packageValid == True:
                        lastAddress = package.address
                        # truckPackages.append(package)
                        truckPackages.insert(i, package)
                        truckPackages.pop(16)
                        packageQue.remove(package)
                        break
            i += 1
        return truckPackages


    def truckDeliverPackages(self, distance, address, truckList, truck):
        route = []
        packageQue = truckList
        i = 0
        lastAddress = 'HUB'
        while i < len(packageQue):
            minDistance = minDistanceFrom(distance, address, lastAddress, packageQue)
            for package in packageQue:
                if package.address == minDistance:
                    lastAddress = package.address
                    route.append(package)
                    packageQue.remove(package)
                    break
        i += 1
        # need to add code that will step through the route and have the truck visit each keeping track of total miles and time
        if truck.ID == 1:
            route.append('HUB')
