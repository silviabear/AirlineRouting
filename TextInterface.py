#! /usr/bin/python
from RoutingGraph import *
import sys
import pprint

routing = RoutingGraph()
def start():
    routing.load()
    while(True):
        print("Please choose the type of your query:")
        print("1. List all cities in the routes")
        print("2.Query of  airlines to/from one city")
        print("3. Statistic of our network")
        print("4. Exit")
        print("Please enter the number of items.")
        line = sys.stdin.readline()
        if(line == "1\n"):
            ListAllCities()
        elif(line == "2\n"):
            Query()
        elif(line == "3\n"):
            Statistic()
        elif(line == "4\n"):
            exit()
        else:
            print("Please enter valid number")
def ListAllCities():
    for city in routing.getCities():
        print routing.getCities()[city]._dict_["name"]
def Query():
    while(True):
        print("Enter the code of city you would like to query:")
        print("Back to main menu, enter b")
        line = sys.stdin.readline()
        line = line[:-1]
        if(line == "b"):
            return;
        city = routing.getCityInfo(line)
        if(city == NULL):
            print("Code does not exist! try again")
            continue
        print "Name: %s"%city._dict_["name"]
        print "Country: %s"%city._dict_["country"]
        print "Continent: %s"%city._dict_["continent"]
        print "Timezone: %s"%city._dict_["timezone"]
        print "Coordinates: ",
        for direction, number in city._dict_["coordinates"].items():
            print "{0:1}: {1:1d}".format(direction, number),
        print
        print "Population: %s"%city._dict_["population"]
        print "Region:%s"%city._dict_["region"]
        print "Reachable Cities: "
        for dest, distance in city._dict_["adj"].items():
            print "City: {0:1} Distance: {1:1d}".format(dest, distance)
def Statistic():
    pass
if __name__ == '__main__':
    start()
