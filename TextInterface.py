#!/usr/bin/python
from RoutingGraph import *
import sys
import webbrowser

routing = RoutingGraph()
def start():
    routing.load()
    while(True):
        print("Please choose the type of your query:")
        print("1. List all cities in the routes")
        print("2.Query of  airlines to/from one city")
        print("3. Statistic of our network")
        print("4. Visualize all our routes")
        print("5. Exit")
        print("Please enter the number of items.")
        line = sys.stdin.readline()
        if(line == "1\n"):
            ListAllCities()
        elif(line == "2\n"):
            Query()
        elif(line == "3\n"):
            Statistic()
        elif(line == "4\n"):
            Visualize()
        elif(line == "5\n"):
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
    flight = routing.getFlightStatistic()
    city = routing.getCityStatistic()
    print "The longest single flight:"
    for ports, distance in flight[0].items():
        print "{0:1}-{1:1}".format(ports.dep, ports.des)
        print "distance: %d"%distance
    print "The shortest single flight:"
    for ports, distance in flight[1].items():
        print "{0:1}-{1:1}".format(ports.dep, ports.des)
        print "distance: %d"%distance
    print "Average distance of flights:"
    print flight[2]
    print "The biggest city we serve:"
    print "Name: %s"%city[0]._dict_["name"]
    print "Population: %d"%city[0]._dict_["population"]
    print "The smallest city we serve:"
    print "Name: %s"%city[1]._dict_["name"]
    print "Population: %d"%city[1]._dict_["population"]
    print "The average size of cities we serve:"
    print city[2]
    print "The cities we serve in continents:"
    for continent, continentCity in city[4].items():
        print "Continent: %s"%continent
        print "Cities: "
        for i in range(len(continentCity.cities)):
            print continentCity.cities[i]._dict_["name"]
    print "Our hub cities:"
    for i in range(len(city[3])):
        print city[3][i]._dict_["name"]
def Visualize():
    url = "http://www.gcmap.com/mapui?P="
    for ports, distance in routing.routes.items():
        url += ports.dep
        url += "-"
        url += ports.des
        url += ","
    url = url[:-1]
    print url
    webbrowser.open(url)
if __name__ == '__main__':
    start()
