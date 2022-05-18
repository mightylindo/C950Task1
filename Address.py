# This class is used to load the address list
import csv

class Address:
    def __init__(self, index, address):
        self.index = index
        self.address = address

    def __str__(self):
        return "%s, %s" % (self.index, self.address)

    def load_address_data(filename, address_list):
        with open(filename) as addressList:
            addressData = csv.reader(addressList, delimiter=',')
            next(addressData)
            for address in addressData:
                ID = address[0]
                aAddress = address[1]

                a = Address(ID, aAddress)
                address_list.append(a)
