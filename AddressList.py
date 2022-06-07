# This is the data structure of the address class
class AddressList:

    def __init__(self): # a simple constructor that creates the address list
        rows, columns = (27, 2)
        self.list = [['' for i in range(columns)]for j in range(rows)]

    def append(self, address): # an append function to add items to the address list
        index = int(address.index)-1
        addressData = address.address
        self.list[index] = addressData

    def search(self, index): # a search function used to find an address in the list based on the index number.
        index = index - 1
        if self.list[index] == '':
            return None

        return self.list[index]

    def searchAddress(self, address): # a search function used to find an address in the list based on the address.
        count = 0
        for item in self.list:
            if item == address:
                return count
            count += 1
        return None
