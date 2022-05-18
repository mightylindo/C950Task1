# This is the datastructure of distance list
class DistanceList:
    # Constructor with optional initial capacity parameter.
    # Assigns all buckets with an empty list.
    def __init__(self):
        rows, columns = (27, 27)
        self.list = [['' for i in range(columns)]for j in range(rows)]

    def append(self, distanceObject):
        row = distanceObject.row
        column = distanceObject.column
        distance = distanceObject.distance

        self.list[row][column] = distance
        self.list[column][row] = distance

    def search(self, row, column):
        if self.list[row][column] == '':
            return None
        return self.list[row][column]
