# This is the datastructure of the address class
class AddressList:

    def __init__(self):
        rows, columns = (27, 2)
        self.list = [['' for i in range(columns)]for j in range(rows)]

    def append(self, address):
        index = int(address.index)-1
        addressData = address.address
        self.list[index] = addressData

    def search(self, index):
        index = index - 1
        if self.list[index] == '':
            return None

        return self.list[index]

    def searchAddress(self, address):
        count = 0
        for item in self.list:
            if item == address:
                return count
            count += 1
        return None
