from DistanceData import *
# This is a simple class that creates a truck object
class Truck():
    def __init__(self, ID):
        self.ID = ID

    def truckLoadPackages(self, distance, address, packageList):
        truckPackages = []
        packageQue = []
        for j in range(40):
            packageQue.append(packageList.search(j+1))
        i = 0
        lastAddress = 'HUB'
        while i < 16:
            minDistance = minDistanceFrom(distance, address, lastAddress, packageQue)
            for package in packageQue:
                if package.address == minDistance:
                    lastAddress = package.address
                    truckPackages.append(package)
                    packageQue.remove(package)
                    break
            i += 1
        return truckPackages
