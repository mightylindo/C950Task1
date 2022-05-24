# This is a simple class that creates a package object.
import csv


class Package:
    def __init__(self, ID, address, deadline, city, zipCode, weight, deliveryStatus):
        self.ID = ID
        self.address = address
        self.deadline = deadline
        self.city = city
        self.zipCode = zipCode
        self.weight = weight
        self.deliveryStatus = deliveryStatus

    # This is an overwrite so that print(Package) will print the values rather than the object reference
    def __str__(self):
        return "%s, %s, %s, %s, %s, %s, %s" % (self.ID, self.address, self.deadline, self.city, self.zipCode, self.weight, self.deliveryStatus)

    def loadPackage(fileName, myHash):
        with open(fileName) as WGUPSPackage:
            packageData = csv.reader(WGUPSPackage, delimiter=',')
            next(packageData)
            # The next command is used to skip the header
            for package in packageData:
                pID = int(package[0])
                pAddress = package[1]
                pDeadline = package[2]
                pCity = package[3]
                pZipCode = package[4]
                pWeight = package[5]
                dStatus = ''

                p = Package(pID, pAddress, pDeadline, pCity, pZipCode, pWeight, dStatus)
                myHash.insert(pID, p)
