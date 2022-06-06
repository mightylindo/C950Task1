import datetime
from ChainingHashTable import *
from Package import *
from Truck import *
from Distance import *
from AddressList import *
from Address import *
from DistanceData import *


def getDistanceData():
    for i in range(27):
        print("Distance: {}".format(distance.search(i, i))) # will always be 0.0 because its going down the line of 0,0; 1,1; 2,2; etc


def getPackageData():
    packageQue = []
    for j in range(40):
        packageQue.append(myHash.search(j + 1))
    return packageQue


def getSpecificPackage(ID):
    packageQue = []
    for j in range(40):
        packageQue.append(myHash.search(j + 1))
    for package in packageQue:
        if package.ID == ID:
            return package
    return None

def getAddressData():
    for i in range(27):
        print("Adderss: {}".format(address.search(i)))


def loadTruckLists():
    packageQue = []
    for j in range(40):
        packageQue.append(myHash.search(j+1))
    truckList1 = truck1.truckLoadPackages(distance, address, packageQue, truck1.ID, myHash, 1)
    truckList2 = truck2.truckLoadPackages(distance, address, packageQue, truck2.ID, myHash, 1)
    truckList = truck1.truckLoadPackages(distance, address, packageQue, truck1.ID, myHash, 2)
    return truckList1, truckList2, truckList


def deliverPackages():
    trip1Miles = truck1.truckDeliverPackages(distance, address, loadTruckLists()[0], truck1, time_obj, 1)
    truck1.miles = trip1Miles[0]
    changes1 = trip1Miles[2]
    truck2Miles = truck2.truckDeliverPackages(distance, address, loadTruckLists()[1], truck2, time_obj, 1)
    truck2.miles = truck2Miles[0]
    changes2 = truck2Miles[2]
    trip2Miles = truck1.truckDeliverPackages(distance, address, loadTruckLists()[2], truck1, time_obj + trip1Miles[1],2)
    truck1.miles = trip2Miles[0]
    changes3 = trip2Miles[2]
    changes = changes1 + changes2 + changes3
    return changes


if __name__ == '__main--':
    print('/nWelcome to C950 Task 1 Package Delivery Program.')

myHash = ChainingHashTable()
distance = DistanceList()
address = AddressList()

Package.loadPackage('WGUPSPackage.csv', myHash)
Distance.loadDistanceData('Distance.csv', distance)
Address.load_address_data('address.csv', address)

time_obj = datetime.datetime(2022,5,24,8,0,0,0)

truck1 = Truck(1, 0)
truck2 = Truck(2, 0)

isExit = True
while(isExit):
    inputs = 0
    print('\nOptions:')
    print('1. Get Truck Lists')
    print('2. Get Total Miles')
    print('3. Get Package Status Report')
    print('4. Get Specific Package')
    print('5. Exit Program')
    option = input('Chose an option (1,2,3,4 or 5): ')
    if option =='1':
        loadTruckLists()
        truckList1 = loadTruckLists()[0]
        truckList2 = loadTruckLists()[1]
        truckList3 = loadTruckLists()[2]
        print(' Truck 1: ')
        for i in range(16):
            print('Package', i + 1, ': ', truckList1[i])
        print(' Truck 2: ')
        for i in range(16):
            print('Package', i + 1, ': ', truckList2[i])
        print(' Truck 3: ')
        for i in range(16):
            print('Package', i + 1, ': ', truckList3[i])
            inputs = inputs + 1
    elif option == '2':
        if inputs == 0:
            changes = deliverPackages()
            for item in changes:
                package = myHash.search(item.ID)
                package.deliveryStatus = item.deliveryStatus
        totalMiles = truck1.miles + truck2.miles
        print(totalMiles, 'Total Miles')
        inputs = inputs + 1
    elif option == '3':
        checkTime = (input('Please input time to check: '))
        if inputs == 0:
            changes = deliverPackages()
            for item in changes:
                package = myHash.search(item.ID)
                package.deliveryStatus = item.deliveryStatus
        packages = getPackageData()
        for thing in packages:
            if thing.deliveryStatus < checkTime:
                thing.deliveryStatus = "Delivered at: " + thing.deliveryStatus
            elif thing.deliveryStatus > checkTime:
                thing.deliveryStatus = 'En route'
            print(thing)
        inputs = inputs + 1
    elif option == '4':
        secondOption = int(input('Please input package ID: '))
        print('ID, Address, City, State, Zipcode, Delivery Deadline, Weight, Special Note, Status')
        print(getSpecificPackage(secondOption))
        inputs = inputs + 1
    elif option == '5':
        isExit = False
    else:
        print('Please select an option 1-4')
