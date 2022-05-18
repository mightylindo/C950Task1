# This class holds the functions that manipulate distance data
from DistanceList import *


def distanceBetween(distanceList, addressList, address1, address2):
    index1 = addressList.searchAddress(address1)
    index2 = addressList.searchAddress(address2)
    distance = float(distanceList.search(index1, index2))
    return distance


def minDistanceFrom(distanceList, addressList, fromAddress, truckPackages):
    minDistance = 100
    for address in truckPackages:
        distance = distanceBetween(distanceList, addressList, fromAddress, address.address)
        if distance < minDistance:
            minDistance = distance
            minAddress = address.address
    return minAddress
