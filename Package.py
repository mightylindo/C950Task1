# This is a simple class that creates a package object.
import csv


class Package: # a constructor that takes in all attributes of package
    def __init__(self, ID, address, city, state, zipCode, deadline,  weight, specialNote, deliveryStatus):
        self.ID = ID
        self.address = address
        self.state = state
        self.city = city
        self.zipCode = zipCode
        self.deadline = deadline
        self.weight = weight
        self.specialNote = specialNote
        self.deliveryStatus = deliveryStatus

    # This is an overwrite so that print(Package) will print the values rather than the object reference
    def __str__(self):
        return "%s, %s, %s, %s, %s, %s, %s, %s, %s" % (self.ID, self.address, self.city, self.state, self.zipCode, self.deadline, self.weight, self.specialNote, self.deliveryStatus)

    # A function that reads information from the csv file and creates a package object and adds it into the Hash Table
    def loadPackage(fileName, myHash):
        with open(fileName) as WGUPSPackage:
            packageData = csv.reader(WGUPSPackage, delimiter=',')
            next(packageData)
            # The next command is used to skip the header
            for package in packageData:
                pID = int(package[0])
                pAddress = package[1]
                pCity = package[2]
                pState = package[3]
                pZipCode = package[4]
                pDeadline = package[5]
                pWeight = package[6]
                pSpecial = package[7]
                dStatus = 'At the HUB'

                p = Package(pID, pAddress, pCity, pState, pZipCode, pDeadline, pWeight, pSpecial, dStatus)
                myHash.insert(pID, p)
