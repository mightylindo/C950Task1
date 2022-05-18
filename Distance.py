# This is a class that will be involve distance data
import csv


class Distance:
    # need to create a distance object that is comprised of a key coordinate pair and a distance value
    # need to create a new key coordinate pair and value from the csv file
    # then need to create the object with the new pair and value and insert it into the list.
    def __init__(self, row, column, distance):
        self.row = row
        self.column = column
        self.distance = distance

    # This is an overwrite so that print(distance) will print the values rather than the object reference
    def __str__(self):
        return "%s,%s, %s" % (self.row, self.column, self.distance)

    def loadDistanceData(filename, myList):
        with open(filename) as distanceFile:
            distanceData = csv.reader(distanceFile)
            next(distanceData)
            r = 0
            for row in distanceData:
                i = 0
                while i < 27:
                    column = i
                    value = row[column]
                    newDistance = Distance(r, column, value)
                    myList.append(newDistance)
                    i += 1
                r += 1
