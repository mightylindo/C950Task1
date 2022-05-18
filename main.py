# This is the main function for this project.
from ChainingHashTable import *
from Package import *
from Greedy import *
from Dijkstra import *
from Truck import *
from Distance import *
from DistanceList import *
from AddressList import *
from Address import *
from DistanceData import *



# This creates an instances of the ChainingHashTable called myHash.
myHash = ChainingHashTable()
distance = DistanceList()
address = AddressList()

Package.loadPackage('WGUPSPackage.csv', myHash)
Distance.loadDistanceData('Distance.csv', distance)
Address.load_address_data('address.csv', address)

def getDistanceData():
    for i in range(27):
        print("Distance: {}".format(distance.search(i, i))) # will always be 0.0 because its going down the line of 0,0; 1,1; 2,2; etc

def getPackageData():
    for i in range(40):
        print("Package: {}".format(myHash.search(i+1)))

def getAddressData():
    for i in range(27):
        print("Adderss: {}".format(address.search(i)))

getDistanceData()
print(distanceBetween(distance, address, 'HUB', '1060 Dalton Ave S'))
'''
print("Distance: {}".format(distance.search(0, 0)))
print("Distance: {}".format(distance.search(0, 25)))
print("Distance: {}".format(distance.search(3, 0)))
print("Distance: {}".format(distance.search(10, 11)))
'''
getPackageData()
getAddressData()
print("Adderss: {}".format(address.search(3)))
print("Adderss: {}".format(address.search(24)))



truck1 = Truck(1)
truckList = truck1.truckLoadPackages(distance, address, myHash)
print(len(truckList))
print(minDistanceFrom(distance, address, 'HUB', truckList))
truck2 = Truck(2)


print("\nGreedy Algorithm: Min Expenses => Max Profits")
greedyAlgorithmMinExpenses(102)  # $102.00 budget
greedyAlgorithmMinExpenses(94)  # $94.00 budget
greedyAlgorithmMinExpenses(71)  # $71.00 budget
greedyAlgorithmMinExpenses(200)  # $200.00 budget


# Dijkstra shortest path main
# Program to find shortest paths from vertex A.
def dijkstraAlgorithmShortestPath():
    g = Graph()

    # add Vertices
    vertex_1 = Vertex("1")
    g.add_vertex(vertex_1)
    vertex_2 = Vertex("2")
    g.add_vertex(vertex_2)
    vertex_3 = Vertex("3")
    g.add_vertex(vertex_3)
    vertex_4 = Vertex("4")
    g.add_vertex(vertex_4)
    vertex_5 = Vertex("5")
    g.add_vertex(vertex_5)
    vertex_6 = Vertex("6")
    g.add_vertex(vertex_6)
    vertex_7 = Vertex("7")
    g.add_vertex(vertex_7)
    vertex_8 = Vertex("8")
    g.add_vertex(vertex_8)
    vertex_9 = Vertex("9")
    g.add_vertex(vertex_9)
    vertex_10 = Vertex("10")
    g.add_vertex(vertex_10)
    vertex_11 = Vertex("11")
    g.add_vertex(vertex_11)
    vertex_12 = Vertex("12")
    g.add_vertex(vertex_12)
    vertex_13 = Vertex("13")
    g.add_vertex(vertex_13)
    vertex_14 = Vertex("14")
    g.add_vertex(vertex_14)
    vertex_15 = Vertex("15")
    g.add_vertex(vertex_15)
    vertex_16 = Vertex("16")
    g.add_vertex(vertex_16)
    vertex_17 = Vertex("17")
    g.add_vertex(vertex_17)
    vertex_18 = Vertex("18")
    g.add_vertex(vertex_18)
    vertex_19 = Vertex("19")
    g.add_vertex(vertex_19)
    vertex_20 = Vertex("20")
    g.add_vertex(vertex_20)
    vertex_21 = Vertex("21")
    g.add_vertex(vertex_21)
    vertex_22 = Vertex("22")
    g.add_vertex(vertex_22)
    vertex_23 = Vertex("23")
    g.add_vertex(vertex_23)
    vertex_24 = Vertex("24")
    g.add_vertex(vertex_24)
    vertex_25 = Vertex("25")
    g.add_vertex(vertex_25)
    vertex_26 = Vertex("26")
    g.add_vertex(vertex_26)
    vertex_27 = Vertex("27")
    g.add_vertex(vertex_27)

    # add 1 Edges
    g.add_undirected_edge(vertex_1, vertex_2, 7.2)
    g.add_undirected_edge(vertex_1, vertex_3, 3.8)
    g.add_undirected_edge(vertex_1, vertex_4, 11.0)
    g.add_undirected_edge(vertex_1, vertex_5, 2.2)
    g.add_undirected_edge(vertex_1, vertex_6, 3.5)
    g.add_undirected_edge(vertex_1, vertex_7, 10.9)
    g.add_undirected_edge(vertex_1, vertex_8, 8.6)
    g.add_undirected_edge(vertex_1, vertex_9, 7.6)
    g.add_undirected_edge(vertex_1, vertex_10, 2.8)
    g.add_undirected_edge(vertex_1, vertex_11, 6.4)
    g.add_undirected_edge(vertex_1, vertex_12, 3.2)
    g.add_undirected_edge(vertex_1, vertex_13, 7.6)
    g.add_undirected_edge(vertex_1, vertex_14, 5.2)
    g.add_undirected_edge(vertex_1, vertex_15, 4.4)
    g.add_undirected_edge(vertex_1, vertex_16, 3.7)
    g.add_undirected_edge(vertex_1, vertex_17, 7.6)
    g.add_undirected_edge(vertex_1, vertex_18, 2.0)
    g.add_undirected_edge(vertex_1, vertex_19, 3.6)
    g.add_undirected_edge(vertex_1, vertex_20, 6.5)
    g.add_undirected_edge(vertex_1, vertex_21, 1.9)
    g.add_undirected_edge(vertex_1, vertex_22, 3.4)
    g.add_undirected_edge(vertex_1, vertex_23, 2.4)
    g.add_undirected_edge(vertex_1, vertex_24, 6.4)
    g.add_undirected_edge(vertex_1, vertex_25, 2.4)
    g.add_undirected_edge(vertex_1, vertex_26, 5.0)
    g.add_undirected_edge(vertex_1, vertex_27, 3.6)
    # add 2 edges
    g.add_undirected_edge(vertex_2, vertex_3, 7.1)
    g.add_undirected_edge(vertex_2, vertex_4, 6.4)
    g.add_undirected_edge(vertex_2, vertex_5, 6.0)
    g.add_undirected_edge(vertex_2, vertex_6, 4.8)
    g.add_undirected_edge(vertex_2, vertex_7, 1.6)
    g.add_undirected_edge(vertex_2, vertex_8, 2.8)
    g.add_undirected_edge(vertex_2, vertex_9, 4.8)
    g.add_undirected_edge(vertex_2, vertex_10, 6.3)
    g.add_undirected_edge(vertex_2, vertex_11, 7.3)
    g.add_undirected_edge(vertex_2, vertex_12, 5.3)
    g.add_undirected_edge(vertex_2, vertex_13, 4.8)
    g.add_undirected_edge(vertex_2, vertex_14, 3.0)
    g.add_undirected_edge(vertex_2, vertex_15, 4.6)
    g.add_undirected_edge(vertex_2, vertex_16, 4.5)
    g.add_undirected_edge(vertex_2, vertex_17, 7.4)
    g.add_undirected_edge(vertex_2, vertex_18, 6.0)
    g.add_undirected_edge(vertex_2, vertex_19, 5.0)
    g.add_undirected_edge(vertex_2, vertex_20, 4.8)
    g.add_undirected_edge(vertex_2, vertex_21, 9.5)
    g.add_undirected_edge(vertex_2, vertex_22, 10.9)
    g.add_undirected_edge(vertex_2, vertex_23, 8.3)
    g.add_undirected_edge(vertex_2, vertex_24, 6.9)
    g.add_undirected_edge(vertex_2, vertex_25, 10.0)
    g.add_undirected_edge(vertex_2, vertex_26, 4.4)
    g.add_undirected_edge(vertex_2, vertex_27, 13.0)
    # add 3 edges
    g.add_undirected_edge(vertex_3, vertex_4, 9.2)
    g.add_undirected_edge(vertex_3, vertex_5, 4.4)
    g.add_undirected_edge(vertex_3, vertex_6, 2.8)
    g.add_undirected_edge(vertex_3, vertex_7, 8.6)
    g.add_undirected_edge(vertex_3, vertex_8, 6.3)
    g.add_undirected_edge(vertex_3, vertex_9, 5.3)
    g.add_undirected_edge(vertex_3, vertex_10, 1.6)
    g.add_undirected_edge(vertex_3, vertex_11, 10.4)
    g.add_undirected_edge(vertex_3, vertex_12, 3.0)
    g.add_undirected_edge(vertex_3, vertex_13, 5.3)
    g.add_undirected_edge(vertex_3, vertex_14, 6.5)
    g.add_undirected_edge(vertex_3, vertex_15, 5.6)
    g.add_undirected_edge(vertex_3, vertex_16, 5.8)
    g.add_undirected_edge(vertex_3, vertex_17, 5.7)
    g.add_undirected_edge(vertex_3, vertex_18, 4.1)
    g.add_undirected_edge(vertex_3, vertex_19, 3.6)
    g.add_undirected_edge(vertex_3, vertex_20, 4.3)
    g.add_undirected_edge(vertex_3, vertex_21, 3.3)
    g.add_undirected_edge(vertex_3, vertex_22, 5.0)
    g.add_undirected_edge(vertex_3, vertex_23, 6.1)
    g.add_undirected_edge(vertex_3, vertex_24, 9.7)
    g.add_undirected_edge(vertex_3, vertex_25, 6.1)
    g.add_undirected_edge(vertex_3, vertex_26, 2.8)
    g.add_undirected_edge(vertex_3, vertex_27, 7.4)
    # add 4 edges
    g.add_undirected_edge(vertex_4, vertex_5, 5.6)
    g.add_undirected_edge(vertex_4, vertex_6, 6.9)
    g.add_undirected_edge(vertex_4, vertex_7, 8.6)
    g.add_undirected_edge(vertex_4, vertex_8, 4.0)
    g.add_undirected_edge(vertex_4, vertex_9, 11.1)
    g.add_undirected_edge(vertex_4, vertex_10, 7.3)
    g.add_undirected_edge(vertex_4, vertex_11, 1.0)
    g.add_undirected_edge(vertex_4, vertex_12, 6.4)
    g.add_undirected_edge(vertex_4, vertex_13, 11.1)
    g.add_undirected_edge(vertex_4, vertex_14, 3.9)
    g.add_undirected_edge(vertex_4, vertex_15, 4.3)
    g.add_undirected_edge(vertex_4, vertex_16, 4.4)
    g.add_undirected_edge(vertex_4, vertex_17, 7.2)
    g.add_undirected_edge(vertex_4, vertex_18, 5.3)
    g.add_undirected_edge(vertex_4, vertex_19, 6.0)
    g.add_undirected_edge(vertex_4, vertex_20, 10.6)
    g.add_undirected_edge(vertex_4, vertex_21, 5.9)
    g.add_undirected_edge(vertex_4, vertex_22, 7.4)
    g.add_undirected_edge(vertex_4, vertex_23, 4.7)
    g.add_undirected_edge(vertex_4, vertex_24, 0.6)
    g.add_undirected_edge(vertex_4, vertex_25, 6.4)
    g.add_undirected_edge(vertex_4, vertex_26, 10.1)
    g.add_undirected_edge(vertex_4, vertex_27, 10.1)
    # add 5 edges
    g.add_undirected_edge(vertex_5, vertex_6, 1.9)
    g.add_undirected_edge(vertex_5, vertex_7, 7.9)
    g.add_undirected_edge(vertex_5, vertex_8, 5.1)
    g.add_undirected_edge(vertex_5, vertex_9, 7.5)
    g.add_undirected_edge(vertex_5, vertex_10, 2.6)
    g.add_undirected_edge(vertex_5, vertex_11, 6.5)
    g.add_undirected_edge(vertex_5, vertex_12, 1.5)
    g.add_undirected_edge(vertex_5, vertex_13, 7.5)
    g.add_undirected_edge(vertex_5, vertex_14, 3.2)
    g.add_undirected_edge(vertex_5, vertex_15, 2.4)
    g.add_undirected_edge(vertex_5, vertex_16, 2.7)
    g.add_undirected_edge(vertex_5, vertex_17, 1.4)
    g.add_undirected_edge(vertex_5, vertex_18, 0.5)
    g.add_undirected_edge(vertex_5, vertex_19, 1.7)
    g.add_undirected_edge(vertex_5, vertex_20, 6.5)
    g.add_undirected_edge(vertex_5, vertex_21, 3.2)
    g.add_undirected_edge(vertex_5, vertex_22, 5.2)
    g.add_undirected_edge(vertex_5, vertex_23, 2.5)
    g.add_undirected_edge(vertex_5, vertex_24, 6.0)
    g.add_undirected_edge(vertex_5, vertex_25, 4.2)
    g.add_undirected_edge(vertex_5, vertex_26, 5.4)
    g.add_undirected_edge(vertex_5, vertex_27, 5.5)
    # add 6 edges
    g.add_undirected_edge(vertex_6, vertex_7, 6.3)
    g.add_undirected_edge(vertex_6, vertex_8, 4.3)
    g.add_undirected_edge(vertex_6, vertex_9, 4.5)
    g.add_undirected_edge(vertex_6, vertex_10, 1.5)
    g.add_undirected_edge(vertex_6, vertex_11, 8.7)
    g.add_undirected_edge(vertex_6, vertex_12, 0.8)
    g.add_undirected_edge(vertex_6, vertex_13, 4.5)
    g.add_undirected_edge(vertex_6, vertex_14, 3.9)
    g.add_undirected_edge(vertex_6, vertex_15, 3.0)
    g.add_undirected_edge(vertex_6, vertex_16, 3.8)
    g.add_undirected_edge(vertex_6, vertex_17, 5.7)
    g.add_undirected_edge(vertex_6, vertex_18, 1.9)
    g.add_undirected_edge(vertex_6, vertex_19, 1.1)
    g.add_undirected_edge(vertex_6, vertex_20, 3.5)
    g.add_undirected_edge(vertex_6, vertex_21, 4.9)
    g.add_undirected_edge(vertex_6, vertex_22, 6.9)
    g.add_undirected_edge(vertex_6, vertex_23, 4.2)
    g.add_undirected_edge(vertex_6, vertex_24, 9.0)
    g.add_undirected_edge(vertex_6, vertex_25, 5.9)
    g.add_undirected_edge(vertex_6, vertex_26, 3.5)
    g.add_undirected_edge(vertex_6, vertex_27, 7.2)
    # add 7 edges
    g.add_undirected_edge(vertex_7, vertex_8, 4.0)
    g.add_undirected_edge(vertex_7, vertex_9, 4.2)
    g.add_undirected_edge(vertex_7, vertex_10, 8.0)
    g.add_undirected_edge(vertex_7, vertex_11, 8.6)
    g.add_undirected_edge(vertex_7, vertex_12, 6.9)
    g.add_undirected_edge(vertex_7, vertex_13, 4.2)
    g.add_undirected_edge(vertex_7, vertex_14, 4.2)
    g.add_undirected_edge(vertex_7, vertex_15, 8.0)
    g.add_undirected_edge(vertex_7, vertex_16, 5.8)
    g.add_undirected_edge(vertex_7, vertex_17, 7.2)
    g.add_undirected_edge(vertex_7, vertex_18, 7.7)
    g.add_undirected_edge(vertex_7, vertex_19, 6.6)
    g.add_undirected_edge(vertex_7, vertex_20, 3.2)
    g.add_undirected_edge(vertex_7, vertex_21, 11.2)
    g.add_undirected_edge(vertex_7, vertex_22, 12.7)
    g.add_undirected_edge(vertex_7, vertex_23, 10.0)
    g.add_undirected_edge(vertex_7, vertex_24, 8.2)
    g.add_undirected_edge(vertex_7, vertex_25, 11.7)
    g.add_undirected_edge(vertex_7, vertex_26, 5.1)
    g.add_undirected_edge(vertex_7, vertex_27, 14.2)
    # add 8 edges
    g.add_undirected_edge(vertex_8, vertex_9, 7.7)
    g.add_undirected_edge(vertex_8, vertex_10, 9.3)
    g.add_undirected_edge(vertex_8, vertex_11, 4.6)
    g.add_undirected_edge(vertex_8, vertex_12, 4.8)
    g.add_undirected_edge(vertex_8, vertex_13, 7.7)
    g.add_undirected_edge(vertex_8, vertex_14, 1.6)
    g.add_undirected_edge(vertex_8, vertex_15, 3.3)
    g.add_undirected_edge(vertex_8, vertex_16, 3.4)
    g.add_undirected_edge(vertex_8, vertex_17, 3.1)
    g.add_undirected_edge(vertex_8, vertex_18, 5.1)
    g.add_undirected_edge(vertex_8, vertex_19, 4.6)
    g.add_undirected_edge(vertex_8, vertex_20, 6.7)
    g.add_undirected_edge(vertex_8, vertex_21, 8.1)
    g.add_undirected_edge(vertex_8, vertex_22, 10.4)
    g.add_undirected_edge(vertex_8, vertex_23, 7.8)
    g.add_undirected_edge(vertex_8, vertex_24, 4.2)
    g.add_undirected_edge(vertex_8, vertex_25, 9.5)
    g.add_undirected_edge(vertex_8, vertex_26, 6.2)
    g.add_undirected_edge(vertex_8, vertex_27, 10.7)
    # add 9 edges
    g.add_undirected_edge(vertex_9, vertex_10, 4.8)
    g.add_undirected_edge(vertex_9, vertex_11, 11.9)
    g.add_undirected_edge(vertex_9, vertex_12, 4.7)
    g.add_undirected_edge(vertex_9, vertex_13, 0.6)
    g.add_undirected_edge(vertex_9, vertex_14, 7.6)
    g.add_undirected_edge(vertex_9, vertex_15, 7.8)
    g.add_undirected_edge(vertex_9, vertex_16, 6.6)
    g.add_undirected_edge(vertex_9, vertex_17, 7.2)
    g.add_undirected_edge(vertex_9, vertex_18, 5.9)
    g.add_undirected_edge(vertex_9, vertex_19, 5.4)
    g.add_undirected_edge(vertex_9, vertex_20, 1.0)
    g.add_undirected_edge(vertex_9, vertex_21, 8.5)
    g.add_undirected_edge(vertex_9, vertex_22, 10.3)
    g.add_undirected_edge(vertex_9, vertex_23, 7.8)
    g.add_undirected_edge(vertex_9, vertex_24, 11.5)
    g.add_undirected_edge(vertex_9, vertex_25, 9.5)
    g.add_undirected_edge(vertex_9, vertex_26, 2.8)
    g.add_undirected_edge(vertex_9, vertex_27, 14.1)
    # add 10 edges
    g.add_undirected_edge(vertex_10, vertex_11, 9.4)
    g.add_undirected_edge(vertex_10, vertex_12, 1.1)
    g.add_undirected_edge(vertex_10, vertex_13, 5.1)
    g.add_undirected_edge(vertex_10, vertex_14, 4.6)
    g.add_undirected_edge(vertex_10, vertex_15, 3.7)
    g.add_undirected_edge(vertex_10, vertex_16, 4.0)
    g.add_undirected_edge(vertex_10, vertex_17, 6.7)
    g.add_undirected_edge(vertex_10, vertex_18, 2.3)
    g.add_undirected_edge(vertex_10, vertex_19, 1.8)
    g.add_undirected_edge(vertex_10, vertex_20, 4.1)
    g.add_undirected_edge(vertex_10, vertex_21, 3.8)
    g.add_undirected_edge(vertex_10, vertex_22, 5.8)
    g.add_undirected_edge(vertex_10, vertex_23, 4.3)
    g.add_undirected_edge(vertex_10, vertex_24, 7.8)
    g.add_undirected_edge(vertex_10, vertex_25, 4.8)
    g.add_undirected_edge(vertex_10, vertex_26, 3.2)
    g.add_undirected_edge(vertex_10, vertex_27, 6.0)
    # add 11 edges
    g.add_undirected_edge(vertex_11, vertex_12, 7.3)
    g.add_undirected_edge(vertex_11, vertex_13, 12.0)
    g.add_undirected_edge(vertex_11, vertex_14, 4.9)
    g.add_undirected_edge(vertex_11, vertex_15, 5.2)
    g.add_undirected_edge(vertex_11, vertex_16, 5.4)
    g.add_undirected_edge(vertex_11, vertex_17, 8.1)
    g.add_undirected_edge(vertex_11, vertex_18, 6.2)
    g.add_undirected_edge(vertex_11, vertex_19, 6.9)
    g.add_undirected_edge(vertex_11, vertex_20, 11.5)
    g.add_undirected_edge(vertex_11, vertex_21, 6.9)
    g.add_undirected_edge(vertex_11, vertex_22, 8.3)
    g.add_undirected_edge(vertex_11, vertex_23, 4.1)
    g.add_undirected_edge(vertex_11, vertex_24, 0.4)
    g.add_undirected_edge(vertex_11, vertex_25, 4.9)
    g.add_undirected_edge(vertex_11, vertex_26, 11.0)
    g.add_undirected_edge(vertex_11, vertex_27, 6.8)
    # add 12 edges
    g.add_undirected_edge(vertex_12, vertex_13, 4.7)
    g.add_undirected_edge(vertex_12, vertex_14, 3.5)
    g.add_undirected_edge(vertex_12, vertex_15, 2.6)
    g.add_undirected_edge(vertex_12, vertex_16, 2.9)
    g.add_undirected_edge(vertex_12, vertex_17, 6.3)
    g.add_undirected_edge(vertex_12, vertex_18, 1.2)
    g.add_undirected_edge(vertex_12, vertex_19, 1.0)
    g.add_undirected_edge(vertex_12, vertex_20, 3.7)
    g.add_undirected_edge(vertex_12, vertex_21, 4.1)
    g.add_undirected_edge(vertex_12, vertex_22, 6.2)
    g.add_undirected_edge(vertex_12, vertex_23, 3.4)
    g.add_undirected_edge(vertex_12, vertex_24, 6.9)
    g.add_undirected_edge(vertex_12, vertex_25, 5.2)
    g.add_undirected_edge(vertex_12, vertex_26, 3.7)
    g.add_undirected_edge(vertex_12, vertex_27, 6.4)
    # add 13 edges
    g.add_undirected_edge(vertex_13, vertex_14, 7.3)
    g.add_undirected_edge(vertex_13, vertex_15, 7.8)
    g.add_undirected_edge(vertex_13, vertex_16, 6.6)
    g.add_undirected_edge(vertex_13, vertex_17, 7.2)
    g.add_undirected_edge(vertex_13, vertex_18, 5.9)
    g.add_undirected_edge(vertex_13, vertex_19, 5.4)
    g.add_undirected_edge(vertex_13, vertex_20, 1.0)
    g.add_undirected_edge(vertex_13, vertex_21, 8.5)
    g.add_undirected_edge(vertex_13, vertex_22, 10.3)
    g.add_undirected_edge(vertex_13, vertex_23, 7.8)
    g.add_undirected_edge(vertex_13, vertex_24, 11.5)
    g.add_undirected_edge(vertex_13, vertex_25, 9.5)
    g.add_undirected_edge(vertex_13, vertex_26, 2.8)
    g.add_undirected_edge(vertex_13, vertex_27, 14.1)
    # add 14 edges
    g.add_undirected_edge(vertex_14, vertex_15, 1.3)
    g.add_undirected_edge(vertex_14, vertex_16, 1.5)
    g.add_undirected_edge(vertex_14, vertex_17, 4.0)
    g.add_undirected_edge(vertex_14, vertex_18, 3.2)
    g.add_undirected_edge(vertex_14, vertex_19, 3.0)
    g.add_undirected_edge(vertex_14, vertex_20, 6.9)
    g.add_undirected_edge(vertex_14, vertex_21, 6.2)
    g.add_undirected_edge(vertex_14, vertex_22, 8.2)
    g.add_undirected_edge(vertex_14, vertex_23, 5.5)
    g.add_undirected_edge(vertex_14, vertex_24, 4.4)
    g.add_undirected_edge(vertex_14, vertex_25, 7.2)
    g.add_undirected_edge(vertex_14, vertex_26, 6.4)
    g.add_undirected_edge(vertex_14, vertex_27, 10.5)
    # add 15 edges
    g.add_undirected_edge(vertex_15, vertex_16, 0.6)
    g.add_undirected_edge(vertex_15, vertex_17, 6.4)
    g.add_undirected_edge(vertex_15, vertex_18, 2.4)
    g.add_undirected_edge(vertex_15, vertex_19, 2.2)
    g.add_undirected_edge(vertex_15, vertex_20, 6.8)
    g.add_undirected_edge(vertex_15, vertex_21, 5.3)
    g.add_undirected_edge(vertex_15, vertex_22, 7.4)
    g.add_undirected_edge(vertex_15, vertex_23, 4.6)
    g.add_undirected_edge(vertex_15, vertex_24, 4.8)
    g.add_undirected_edge(vertex_15, vertex_25, 6.3)
    g.add_undirected_edge(vertex_15, vertex_26, 6.5)
    g.add_undirected_edge(vertex_15, vertex_27, 8.8)
    # add 16 edges
    g.add_undirected_edge(vertex_16, vertex_17, 5.6)
    g.add_undirected_edge(vertex_16, vertex_18, 1.6)
    g.add_undirected_edge(vertex_16, vertex_19, 1.7)
    g.add_undirected_edge(vertex_16, vertex_20, 6.4)
    g.add_undirected_edge(vertex_16, vertex_21, 4.9)
    g.add_undirected_edge(vertex_16, vertex_22, 6.9)
    g.add_undirected_edge(vertex_16, vertex_23, 4.2)
    g.add_undirected_edge(vertex_16, vertex_24, 5.6)
    g.add_undirected_edge(vertex_16, vertex_25, 5.9)
    g.add_undirected_edge(vertex_16, vertex_26, 5.7)
    g.add_undirected_edge(vertex_16, vertex_27, 8.4)
    # add 17 edges
    g.add_undirected_edge(vertex_17, vertex_18, 7.1)
    g.add_undirected_edge(vertex_17, vertex_19, 6.1)
    g.add_undirected_edge(vertex_17, vertex_20, 7.2)
    g.add_undirected_edge(vertex_17, vertex_21, 10.6)
    g.add_undirected_edge(vertex_17, vertex_22, 12.0)
    g.add_undirected_edge(vertex_17, vertex_23, 9.4)
    g.add_undirected_edge(vertex_17, vertex_24, 7.5)
    g.add_undirected_edge(vertex_17, vertex_25, 11.1)
    g.add_undirected_edge(vertex_17, vertex_26, 6.2)
    g.add_undirected_edge(vertex_17, vertex_27, 13.6)
    # add 18 edges
    g.add_undirected_edge(vertex_18, vertex_19, 1.6)
    g.add_undirected_edge(vertex_18, vertex_20, 4.9)
    g.add_undirected_edge(vertex_18, vertex_21, 3.0)
    g.add_undirected_edge(vertex_18, vertex_22, 5.0)
    g.add_undirected_edge(vertex_18, vertex_23, 2.3)
    g.add_undirected_edge(vertex_18, vertex_24, 5.5)
    g.add_undirected_edge(vertex_18, vertex_25, 4.0)
    g.add_undirected_edge(vertex_18, vertex_26, 5.1)
    g.add_undirected_edge(vertex_18, vertex_27, 5.2)
    # add 19 edges
    g.add_undirected_edge(vertex_19, vertex_20, 4.4)
    g.add_undirected_edge(vertex_19, vertex_21, 4.6)
    g.add_undirected_edge(vertex_19, vertex_22, 6.6)
    g.add_undirected_edge(vertex_19, vertex_23, 3.9)
    g.add_undirected_edge(vertex_19, vertex_24, 6.5)
    g.add_undirected_edge(vertex_19, vertex_25, 5.6)
    g.add_undirected_edge(vertex_19, vertex_26, 4.3)
    g.add_undirected_edge(vertex_19, vertex_27, 6.9)
    # add 20 edges
    g.add_undirected_edge(vertex_20, vertex_21, 7.5)
    g.add_undirected_edge(vertex_20, vertex_22, 9.3)
    g.add_undirected_edge(vertex_20, vertex_23, 6.8)
    g.add_undirected_edge(vertex_20, vertex_24, 11.4)
    g.add_undirected_edge(vertex_20, vertex_25, 8.5)
    g.add_undirected_edge(vertex_20, vertex_26, 1.8)
    g.add_undirected_edge(vertex_20, vertex_27, 13.1)
    # add 21 edges
    g.add_undirected_edge(vertex_21, vertex_22, 2.0)
    g.add_undirected_edge(vertex_21, vertex_23, 2.9)
    g.add_undirected_edge(vertex_21, vertex_24, 6.4)
    g.add_undirected_edge(vertex_21, vertex_25, 2.8)
    g.add_undirected_edge(vertex_21, vertex_26, 6.0)
    g.add_undirected_edge(vertex_21, vertex_27, 4.1)
    # add 22 edges
    g.add_undirected_edge(vertex_22, vertex_23, 4.4)
    g.add_undirected_edge(vertex_22, vertex_24, 7.9)
    g.add_undirected_edge(vertex_22, vertex_25, 3.4)
    g.add_undirected_edge(vertex_22, vertex_26, 7.9)
    g.add_undirected_edge(vertex_22, vertex_27, 4.7)
    # add 23 edges
    g.add_undirected_edge(vertex_23, vertex_24, 4.5)
    g.add_undirected_edge(vertex_23, vertex_25, 1.7)
    g.add_undirected_edge(vertex_23, vertex_26, 6.8)
    g.add_undirected_edge(vertex_23, vertex_27, 3.1)
    # add 24 edges
    g.add_undirected_edge(vertex_24, vertex_25, 5.4)
    g.add_undirected_edge(vertex_24, vertex_26, 10.6)
    g.add_undirected_edge(vertex_24, vertex_27, 7.8)
    # add 25 edges
    g.add_undirected_edge(vertex_25, vertex_26, 7.0)
    g.add_undirected_edge(vertex_25, vertex_27, 1.3)
    # add 26 edges
    g.add_undirected_edge(vertex_26, vertex_27, 8.3)

    # Run Dijkstra's algorithm first.
    dijkstra_shortest_path(g, vertex_3)

    # Get the vertices by the label for convenience; display shortest path for each vertex
    # from vertex_1.
    print("\nDijkstra shortest path:")
    for v in g.adjacency_list:
        if v.pred_vertex is None and v is not vertex_3:
            print("3 to %s ==> no path exists" % v.label)
        else:
            print("3 to %s ==> %s (total distance: %g)" % (v.label, get_shortest_path(vertex_3, v), v.distance))


dijkstraAlgorithmShortestPath()
