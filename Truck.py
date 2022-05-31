import datetime

from DistanceData import *
from Dijkstra import *
# This is a simple class that creates a truck object
class Truck():
    def __init__(self, ID, miles):
        self.ID = ID
        self.miles = miles

    def truckLoadPackages(self, distance, address, packageList, truck, myHash):
        truckPackages = ['','','','','','','','','','','','','','','','']
        replacmentList = []
        i = 0
        lastAddress = 'HUB'
        if truck == 2:
            truck2Packages = []
            for j in range(40):
                p = myHash.search(j+1)
                if p.specialNote == 'Can only be on truck 2':
                    truck2Packages.append(p)
            truckPackages.insert(0, truck2Packages[0])
            truckPackages.pop(16)
            truckPackages.insert(1, truck2Packages[1])
            truckPackages.pop(16)
            truckPackages.insert(2, truck2Packages[2])
            truckPackages.pop(16)
            truckPackages.insert(3, truck2Packages[3])
            truckPackages.pop(16)
            i = 4
        while i < len(truckPackages):
            if len(packageList) > 0:
                minDistance = minDistanceFrom(distance, address, lastAddress, packageList)
            for package in packageList:
                if package.address == minDistance:
                    if package.specialNote == 'Can only be on truck 2':
                        i = i - 1
                        replacmentList.append(package)
                        packageList.remove(package)
                        break
                    if package.specialNote == '':
                       # pack = myHash.search(package.ID)
                       # pack.deliveryStatus = 'en Route'
                        lastAddress = package.address
                        # truckPackages.append(package)
                        truckPackages.insert(i, package)
                        truckPackages.pop(16)
                        packageList.remove(package)
                        break
                    elif package.specialNote == 'Must be delivered with 15, 19':
                        lastAddress = package.address
                        # truckPackages.append(package)
                        truckPackages.insert(i, package)
                        truckPackages.pop(16)
                        packageList.remove(package)
                        break
                    elif package.specialNote == 'Must be delivered with 13, 19':
                        lastAddress = package.address
                        # truckPackages.append(package)
                        truckPackages.insert(i, package)
                        truckPackages.pop(16)
                        packageList.remove(package)
                        break
                    elif package.specialNote == 'Must be delivered with 13, 15':
                        lastAddress = package.address
                        # truckPackages.append(package)
                        truckPackages.insert(i, package)
                        truckPackages.pop(16)
                        packageList.remove(package)
                        break
                    elif package.specialNote == 'Delayed on flight---will not arrive to depot until 9:05 am':
                        if truck == 3:
                            lastAddress = package.address
                            # truckPackages.append(package)
                            truckPackages.insert(i, package)
                            truckPackages.pop(16)
                            packageList.remove(package)
                            break
                        else:
                            i = i - 1
                            replacmentList.append(package)
                            packageList.remove(package)
                            break
                    elif package.specialNote == 'Wrong address listed':
                        if truck == 3:
                            lastAddress = package.address
                            # truckPackages.append(package)
                            truckPackages.insert(i, package)
                            truckPackages.pop(16)
                            packageList.remove(package)
                            break
                        else:
                            i = i - 1
                            replacmentList.append(package)
                            packageList.remove(package)
                            break
                    '''elif package.specialNote == 'Can only be on truck 2':
                        if truck == 2:
                            lastAddress = package.address
                            # truckPackages.append(package)
                            truckPackages.insert(i, package)
                            truckPackages.pop(16)
                            packageList.remove(package)
                            break
                        else:
                            i = i - 1
                            replacmentList.append(package)
                            packageList.remove(package)
                            break
                            '''
            i += 1
        for pack in replacmentList:
            packageList.append(pack)
        return truckPackages


    def truckDeliverPackages(self, distance, address, truckList, truck, startTime, myHash):
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
                deliveryTime = startTime + timeToDeliver #this works just need to find a way to pass it to the hashtable
                package = myHash.search(i.ID)
                if package.deadline == 'EOD':
                    deadline = datetime.datetime(2022,5,24,17,0,0,0)
                    if deadline > deliveryTime:
                        package.deliveryStatus = "Delivered on time at: " + str(deliveryTime)
                    elif deadline < deliveryTime:
                        package.deliveryStatus = "LATE delivery at: " + str(deliveryTime)
                elif package.deadline == '9:00 AM':
                    deadline = datetime.datetime(2022, 5, 24, 9, 0, 0, 0)
                    if deadline > deliveryTime:
                        package.deliveryStatus = "Delivered on time at: " + str(deliveryTime)
                    elif deadline < deliveryTime:
                        package.deliveryStatus = "LATE delivery at: " + str(deliveryTime)
                elif package.deadline == '10:30 AM':
                    deadline = datetime.datetime(2022, 5, 24, 10, 30, 0, 0)
                    if deadline > deliveryTime:
                        package.deliveryStatus = "Delivered on time at: " + str(deliveryTime)
                    elif deadline < deliveryTime:
                        package.deliveryStatus = "LATE delivery at: " + str(deliveryTime)
                startAddress = i.address
                route.remove(i)
        if truck.ID == 1:
             totalTruckMiles = totalTruckMiles + distanceBetween(distance, address, startAddress, 'HUB')
        return totalTruckMiles
