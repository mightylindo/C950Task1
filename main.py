# This is the main file for package delivery program for task C950
# Author: Jordan Lindorff Student ID: 001460491
# This program takes 3 csv files as input and produces a plan to deliver all packages listed on time and under 140 miles
# It also takes into account any special notes listed on the package list

import datetime
from ChainingHashTable import *
from Package import *
from Truck import *
from Distance import *
from AddressList import *
from Address import *
from DistanceData import *

# This function is used to print all items stored in the hash table.
def getAllPackages():
    for j in range(40):
        print("Package: {}".format(myHash.search(j+1)))

# This function returns a list of all items stored in the hash table.
def getPackageData():
    packageQue = []
    for j in range(40):
        packageQue.append(myHash.search(j + 1))
    return packageQue

# This function takes an int ID as input and puts all items in the hash table in a list, then it loops through the list
# and returns the package info for the package with a matching ID, if none is found it returns None
def getSpecificPackage(ID):
    packageQue = []
    for j in range(40):
        packageQue.append(myHash.search(j + 1))
    for package in packageQue:
        if package.ID == ID:
            return package
    return None

# This function is used to print all the addresses listed in the address list datastructure. This was mostly used for
# testing, and is not used in the main program
def getAddressData():
    for i in range(27):
        print("Adderss: {}".format(address.search(i)))

# This is the function called for loading the trucks. This function puts all items stored in the Hash Table into a
# list. It then calls the truckLoadPackages function for each of the loads, truck1 trip 1, truck 2, and truck 1 trip 2.
# The function then returns a list of the three truck lists which will be used by the deliverPackages function.
def loadTruckLists():
    packageQue = []
    for j in range(40):
        packageQue.append(myHash.search(j+1))
    truckList1 = truck1.truckLoadPackages(distance, address, packageQue, truck1.ID, myHash, 1)
    truckList2 = truck2.truckLoadPackages(distance, address, packageQue, truck2.ID, myHash, 1)
    truckList = truck1.truckLoadPackages(distance, address, packageQue, truck1.ID, myHash, 2)
    return truckList1, truckList2, truckList

# This function is called to deliver the packages. This function will call the truckDeliverPackages function for each of
# the trips. This function then catches the total miles for each tip as well as any changes to the package data.
# It then combines all the changes into a single list and returns them. The total miles are stored within the truck
# objects.
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

# This is the main function for this program. It makes all the function called needed based on the users input.
if __name__ == '__main--':
    print('/nWelcome to C950 Task 1 Package Delivery Program.')

myHash = ChainingHashTable() # an instance of the ChainingHashTable data structure class
distance = DistanceList() # an instance of the DistanceList data structure class
address = AddressList() # an instance of the AddressList data structure class

# Loads the Hash Table with the information in the Package csv file
Package.loadPackage('WGUPSPackage.csv', myHash)
# Loads the DistanceList with the information in the distance csv file
Distance.loadDistanceData('Distance.csv', distance)
# Loads the AddressList with the information in the address csv file
Address.load_address_data('address.csv', address)

time_obj = datetime.datetime(2022,5,24,8,0,0,0) # the start time for the program

truck1 = Truck(1, 0) # Creating truck object 1
truck2 = Truck(2, 0) # Creating truck object 2

isExit = True # a boolean flag used to keep the program up until the user selects exit.
while(isExit):
    inputs = 0 # This is a simple counter of how many commands have been issued
    # The interface prints out this screen for the various options
    print('\nOptions:')
    print('1. Get Truck Lists')
    print('2. Get Total Miles')
    print('3. Get Package Status Report')
    print('4. Get Specific Package')
    print('5. Exit Program')
    option = input('Chose an option (1,2,3,4 or 5): ')
    if option =='1': # displays the three loads and which packages are on each.
        truckList1 = loadTruckLists()[0]
        truckList2 = loadTruckLists()[1]
        truckList3 = loadTruckLists()[2]
        print(' Truck 1 Trip 1: ')
        for i in range(16):
            print('Package', i + 1, ': ', truckList1[i])
        print(' Truck 2: ')
        for i in range(16):
            print('Package', i + 1, ': ', truckList2[i])
        print(' Truck 1 Trip 2: ')
        for i in range(16):
            print('Package', i + 1, ': ', truckList3[i])
            inputs = inputs + 1
    # This displays all the package info after the day is complete with the delivery times and also
    # shows the total miles traveled.
    elif option == '2':
        if inputs == 0:
            # This calls the deliverPackages function which will return a list of changes to the package data,
            # namely the time it was delivered.
            changes = deliverPackages()
            for item in changes: #This loops through the changes and applies them to the Hash Table
                package = myHash.search(item.ID)
                package.deliveryStatus = item.deliveryStatus
        totalMiles = truck1.miles + truck2.miles # This collects the total miles from the truck objects
        getAllPackages() # This calls the function that prints out all the package data
        print(totalMiles, 'Total Miles') # This prints the total miles.
        inputs = inputs + 1
    # This option if selected then asks for a time to check in the HH:MM:SS format. It will then display a status report
    # based on the time entered.
    elif option == '3':
        checkTime = (input('Please input time to check(format HH:MM:SS): '))
        secondTime = '09:00:20' # This is when the truck 1 trip 2 starts
        truck3 = loadTruckLists()[2]
        if inputs == 0:
            changes = deliverPackages()
            for item in changes:
                package = myHash.search(item.ID)
                package.deliveryStatus = item.deliveryStatus
        # This calls the function that collects all the data stored in the Hash Table and returns it in a list
        packages = getPackageData()
        for thing in packages: # This loops through all the packages and checks the delivery times against the checktime
            deliveryTime = str(thing.deliveryStatus.time())
            if deliveryTime < checkTime:
                thing.deliveryStatus = "Delivered at: " + str(thing.deliveryStatus)
            elif deliveryTime > checkTime:
                thing.deliveryStatus = 'En route'
                if truck3.__contains__(thing): # this checks if the package is part of the 3rd load
                    # This checks if the delivery time is before or after the start time of the last load
                    if deliveryTime < secondTime:
                        thing.deliveryStatus = 'At the HUB'
            print(thing)
        inputs = inputs + 1
        # If this option is selected it then requests a package ID and returns the information for that specific package
    elif option == '4':
        secondOption = int(input('Please input package ID: '))
        print('ID, Address, City, State, Zipcode, Delivery Deadline, Weight, Special Note, Status')
        print(getSpecificPackage(secondOption))
        inputs = inputs + 1
    elif option == '5': # This option is used to exit the program.
        isExit = False
    else:
        print('Please select an option 1-4')
