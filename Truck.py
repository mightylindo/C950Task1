import datetime

from DistanceData import *
from Dijkstra import *
# This is a simple class that creates a truck object
class Truck():
    def __init__(self, ID, miles):
        self.ID = ID
        self.miles = miles

    def truckLoadPackages(self, distance, address, packageList, truck):
        truckPackages = ['','','','','','','','','','','','','','','','']
        i = 0
        lastAddress = 'HUB'
        while i < len(truckPackages):
            packageValid = False
            if len(packageList) > 0:
                minDistance = minDistanceFrom(distance, address, lastAddress, packageList)
            for package in packageList:
                if package.address == minDistance:
                    '''
                    if truck == 2:
                        if package.ID == 3 or 18 or 36 or 38: # this is not working
                            packageValid = True
                    '''
                    packageValid = True
                    if packageValid == True:
                        lastAddress = package.address
                        # truckPackages.append(package)
                        truckPackages.insert(i, package)
                        truckPackages.pop(16)
                        packageList.remove(package)
                        break
            i += 1
        return truckPackages


    def truckDeliverPackages(self, distance, address, truckList, truck, startTime):
        route = []
        packageQue = truckList
        count = 15
        time = startTime
        while count > 0:
            if packageQue[count] == '':
                packageQue.pop(count)
            count = count - 1
        i = 0
        lastAddress = 'HUB'
        # need to remove the extra code below as teh truck list is already sorted by closest to the HUB.
        # Need to create a graph of all 16 packages
        # need to find the shortest path possible while visiting every path

        while i < len(packageQue):
            if len(packageQue) > 0:
                minDistance = minDistanceFrom(distance, address, lastAddress, packageQue)
            for package in packageQue:
                if package.address == minDistance:
                    lastAddress = package.address
                    route.append(package)
                    packageQue.remove(package)
                    break
        i += 1
        # need to add code that will step through the route and have the truck visit each keeping track of total miles and time
        startAddress = 'HUB'
        totalTruckMiles = truck.miles
        while len(route) > 0:
            for i in route:
                addMiles = distanceBetween(distance, address, startAddress, i.address)
                totalTruckMiles = totalTruckMiles + addMiles
                timeToDeliver = datetime.timedelta(hours=totalTruckMiles/18)
                #print(timeToDeliver)
                #print(startTime)
                deliveryTime = startTime + timeToDeliver #this works just need to find a way to pass it to the hashtable
                i.deliveryStatus = deliveryTime
                #print(deliveryTime)
                startAddress = i.address
                route.remove(i)
        if truck.ID == 1:
             totalTruckMiles = totalTruckMiles + distanceBetween(distance, address, startAddress, 'HUB')
        return totalTruckMiles
