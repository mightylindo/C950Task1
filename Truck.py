import datetime
from DistanceData import *

# This is a simple class that creates a truck object
class Truck():
    def __init__(self, ID, miles):
        self.ID = ID
        self.miles = miles

    # This function takes the distanceList, addressList, a package List, a truck object, the Hash Table, and an int trip
    # as input. It returns a load plan for the given truck based on the package list.
    def truckLoadPackages(self, distance, address, packageList, truck, myHash, trip):
        truckPackages = ['','','','','','','','','','','','','','','','']  # Creates a list with a len of 16
        replacmentList = []  # and empty list used to replace packages back into the package list
        groupedList = []  # and empty list used for the packages that must be grouped together
        i = 0  # a simple counter
        lastAddress = 'HUB'  # the starting address
        if truck == 1:
            if trip == 1:
                # this loops through all the packages and finds the 8 listed below and inserts them into the
                # grouped list
                for k in range(40):
                    p = myHash.search(k + 1)
                    if p.ID == 15:
                        groupedList.insert(0, p)
                    if p.ID == 16:
                        groupedList.insert(1, p)
                    if p.ID == 14:
                        groupedList.insert(2, p)
                    if p.ID == 19:
                        groupedList.insert(3, p)
                    if p.ID == 20:
                        groupedList.insert(4, p)
                    if p.ID == 40:
                        groupedList.insert(5, p)
                    if p.ID == 1:
                        groupedList.insert(6, p)
                    if p.ID == 13:
                        groupedList.insert(7, p)
                # then the below code inserts the groupedList into the truck packages List and returns the
                # list for truck 1 trip 1
                truckPackages.insert(0, groupedList[0])
                truckPackages.pop(16)
                truckPackages.insert(1, groupedList[1])
                truckPackages.pop(16)
                truckPackages.insert(2, groupedList[7])
                truckPackages.pop(16)
                truckPackages.insert(3, groupedList[3])
                truckPackages.pop(16)
                truckPackages.insert(4, groupedList[4])
                truckPackages.pop(16)
                truckPackages.insert(5, groupedList[5])
                truckPackages.pop(16)
                truckPackages.insert(6, groupedList[2])
                truckPackages.pop(16)
                truckPackages.insert(7, groupedList[6])
                truckPackages.pop(16)
                return truckPackages
            else: # This is for truck1 trip 2
                for k in range(40): # this loop adds all the delayed and wrong address packages
                    p = myHash.search(k + 1)
                    if p.ID == 6:
                        groupedList.insert(0, p)
                    if p.ID == 25:
                        groupedList.insert(1, p)
                    if p.ID == 28:
                        groupedList.insert(2, p)
                    if p.ID == 32:
                        groupedList.insert(3, p)
                    if p.ID == 9:
                        groupedList.insert(4, p)
                # below code adds them to the truck packages list
                truckPackages.insert(0, groupedList[0])
                truckPackages.pop(16)
                truckPackages.insert(1, groupedList[1])
                truckPackages.pop(16)
                truckPackages.insert(2, groupedList[2])
                truckPackages.pop(16)
                truckPackages.insert(3, groupedList[3])
                truckPackages.pop(16)
                truckPackages.insert(4, groupedList[4])
                truckPackages.pop(16)
                # we change i to = 5 so that when we go to add the rest of the packages to the list we know where to
                # start
                i = 5
        if truck == 2: #
            truck2Packages = []
            # The loop finds all the truck 2 and early delivery time packages listed below and
            # adds them to truck2packages
            for j in range(40):
                p = myHash.search(j+1)
                if p.ID == 29:
                    truck2Packages.insert(0, p)
                if p.ID == 30:
                    truck2Packages.insert(1, p)
                if p.ID == 31:
                    truck2Packages.insert(2, p)
                if p.ID == 34:
                    truck2Packages.insert(3, p)
                if p.ID == 37:
                    truck2Packages.insert(4, p)
                if p.ID == 38:
                    truck2Packages.insert(5, p)
                if p.ID == 36:
                    truck2Packages.insert(6, p)
                if p.ID == 3:
                    truck2Packages.insert(7, p)
                if p.ID == 18:
                    truck2Packages.insert(8, p)
            # The below adds truck2Packages to the truckPackages list
            truckPackages.insert(0, truck2Packages[0])
            truckPackages.pop(16)
            truckPackages.insert(1, truck2Packages[1])
            truckPackages.pop(16)
            truckPackages.insert(2, truck2Packages[2])
            truckPackages.pop(16)
            truckPackages.insert(3, truck2Packages[3])
            truckPackages.pop(16)
            truckPackages.insert(4, truck2Packages[4])
            truckPackages.pop(16)
            truckPackages.insert(5, truck2Packages[5])
            truckPackages.pop(16)
            truckPackages.insert(6, truck2Packages[6])
            truckPackages.pop(16)
            truckPackages.insert(7, truck2Packages[7])
            truckPackages.pop(16)
            truckPackages.insert(8, truck2Packages[8])
            truckPackages.pop(16)
            # we change i to = 9 so that when we go to add the rest of the packages to the list we know where to
            # start
            i = 9
        while i < len(truckPackages): # we do this while i is < the len of the truckPackages list
            if len(packageList) > 0:
                # this call finds the minimum distance for the lastAddress and packages remaining in the packageList
                minDistance = minDistanceFrom(distance, address, lastAddress, packageList)
            for package in packageList: # this loops through and adds packages to the list based on min distance
                if package.address == minDistance:
                    # all these if/ elif statements make sure that we don't add any preselected packages to the list,
                    # thus preventing duplication in the list
                    if package.ID == 15:
                        i = i - 1
                        replacmentList.append(package)
                        packageList.remove(package)
                        break
                    elif package.ID == 16:
                        i = i - 1
                        replacmentList.append(package)
                        packageList.remove(package)
                        break
                    elif package.ID == 14:
                        i = i - 1
                        replacmentList.append(package)
                        packageList.remove(package)
                        break
                    elif package.ID == 19:
                        i = i - 1
                        replacmentList.append(package)
                        packageList.remove(package)
                        break
                    elif package.ID == 20:
                        i = i - 1
                        replacmentList.append(package)
                        packageList.remove(package)
                        break
                    elif package.ID == 40:
                        i = i - 1
                        replacmentList.append(package)
                        packageList.remove(package)
                        break
                    elif package.ID == 1:
                        i = i - 1
                        replacmentList.append(package)
                        packageList.remove(package)
                        break
                    elif package.ID == 13:
                        i = i - 1
                        replacmentList.append(package)
                        packageList.remove(package)
                        break
                    elif package.ID == 6:
                        i = i - 1
                        replacmentList.append(package)
                        packageList.remove(package)
                        break
                    elif package.ID == 25:
                        i = i - 1
                        replacmentList.append(package)
                        packageList.remove(package)
                        break
                    elif package.ID == 28:
                        i = i - 1
                        replacmentList.append(package)
                        packageList.remove(package)
                        break
                    elif package.ID == 32:
                        i = i - 1
                        replacmentList.append(package)
                        packageList.remove(package)
                        break
                    elif package.ID == 9:
                        i = i - 1
                        replacmentList.append(package)
                        packageList.remove(package)
                        break
                    elif package.ID == 29:
                        i = i - 1
                        replacmentList.append(package)
                        packageList.remove(package)
                        break
                    elif package.ID == 30:
                        i = i - 1
                        replacmentList.append(package)
                        packageList.remove(package)
                        break
                    elif package.ID == 31:
                        i = i - 1
                        replacmentList.append(package)
                        packageList.remove(package)
                        break
                    elif package.ID == 34:
                        i = i - 1
                        replacmentList.append(package)
                        packageList.remove(package)
                        break
                    elif package.ID == 37:
                        i = i - 1
                        replacmentList.append(package)
                        packageList.remove(package)
                        break
                    elif package.ID == 38:
                        i = i - 1
                        replacmentList.append(package)
                        packageList.remove(package)
                        break
                    elif package.ID == 36:
                        i = i - 1
                        replacmentList.append(package)
                        packageList.remove(package)
                        break
                    elif package.ID == 3:
                        i = i - 1
                        replacmentList.append(package)
                        packageList.remove(package)
                        break
                    elif package.ID == 18:
                        i = i - 1
                        replacmentList.append(package)
                        packageList.remove(package)
                        break

                    # This checks that there is no special note and adds the package to the truck list, changes the
                    # lastAddress to the package's address. Once the package is added to truck list the function pop the
                    # last index to get rid of the place holder, then the function removes the package from the package
                    # list and breaks the loop
                    if package.specialNote == '':
                        lastAddress = package.address
                        truckPackages.insert(i, package)
                        truckPackages.pop(16)
                        packageList.remove(package)
                        break
            i += 1
        # this loops the the replacement list and adds them back to the package list once the truck list for this
        # load is created.
        for pack in replacmentList:
            packageList.append(pack)
        return truckPackages # returns the list

    # This function takes the distanceList, addressList, the truckList created by the loadTrucks Function, a truck
    # object, a start time, and a trip number. It then returns the total miles, the changes to the packages,
    # and the time it took to deliver all packages
    def truckDeliverPackages(self, distance, address, truckList, truck, startTime, trip):
        route = truckList
        packageChanges = []
        count = 15
        # This while loop is used to pop any empty items from the route list. Primarily there for truck 1 trip 1
        while count > 0:
            if route[count] == '':
                route.pop(count)
            count = count - 1
        i = 0
        startAddress = 'HUB'
        totalTruckMiles = 0 # Sets this trips miles to 0 before beginning.
        while i < len(route):
            package = route[i]
            # This gets the miles between the start address and the packages address
            addMiles = distanceBetween(distance, address, startAddress, package.address)
            # The function then adds the distance to the total miles driven
            totalTruckMiles = totalTruckMiles + addMiles
            # The time to deliver is calculated by taking the total miles driven and dividing it by the speed
            timeToDeliver = datetime.timedelta(hours=totalTruckMiles/18)
            # the delivery time is then calculated by adding the time to deliver to the start time
            deliveryTime = startTime + timeToDeliver
            # The function then stores the delivery time in the delivery status attribute of the package
            package.deliveryStatus = deliveryTime
            # next the function changes the start address to the package address
            startAddress = package.address
            # The function then adds the package to the packageChanges list
            packageChanges.append(package)
            # And then the package is removed from route
            route.remove(package)
        if truck.ID == 1:
            if trip == 1: # If its truck 1's first trip then we add the miles back to the HUB to the total.
                totalTruckMiles = totalTruckMiles + distanceBetween(distance, address, startAddress, 'HUB')
        return totalTruckMiles, timeToDeliver, packageChanges

