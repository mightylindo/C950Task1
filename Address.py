# This class is used to create address objects adn to load the address list with address objects
import csv

class Address:
    def __init__(self, index, address): # A simple constructor for the address object
        self.index = index
        self.address = address

    def __str__(self): # a simple overwrite to display the objects attributes
        return "%s, %s" % (self.index, self.address)

    # This is a simple function that reads the information from the address csv and creates an address object and adds
    # it to the address list.
    def load_address_data(filename, address_list):
        with open(filename) as addressList:
            addressData = csv.reader(addressList, delimiter=',')
            next(addressData)
            for address in addressData:
                ID = address[0]
                aAddress = address[1]

                a = Address(ID, aAddress)
                address_list.append(a)
