# This is a class that will create the distance objects and that will add them to the distance list.
import csv


class Distance:
    def __init__(self, row, column, distance): # a simple constructor for the distance object
        self.row = row
        self.column = column
        self.distance = distance

    # This is an overwrite so that print(distance) will print the values rather than the object reference
    def __str__(self):
        return "%s,%s, %s" % (self.row, self.column, self.distance)

    # This function reads information from the csv file and creates a new distance object and adds it to the distance
    # list.
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
