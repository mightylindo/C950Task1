# This class holds the functions that manipulate distance data
from DistanceList import *

# This function takes the distance list, the address list, and two address as input and returns the distance
# between the two address.
def distanceBetween(distanceList, addressList, address1, address2):
    index1 = addressList.searchAddress(address1) # Finds the index based on the address
    index2 = addressList.searchAddress(address2) # Finds the index based on the address
    # Searches the distance list for the two indexes and returns the distance
    distance = float(distanceList.search(index1, index2))
    return distance

# This function takes the distance list, the address list, a start address, and a list of packages as input.
# It then returns the address in the package list that is closest to the start address.
def minDistanceFrom(distanceList, addressList, fromAddress, truckPackages):
    minDistance = 100
    for address in truckPackages: # Loops through all the packages and calls distance between
        distance = distanceBetween(distanceList, addressList, fromAddress, address.address)
        # Compare the distance between against the min address, if distance is smaller it becomes the min distance and
        # the min address is changed to be that packages address
        if distance < minDistance:
            minDistance = distance
            minAddress = address.address
    return minAddress
