from RoutingGraph import *
import sys
import webbrowser
from boto.roboto.awsqueryrequest import Line

routing = RoutingGraph()
def start():
    routing.load()
    while(True):
        print("Please choose the type of your query:")
        print("1. List all cities in the routes")
        print("2.Query of  airlines to/from one city")
        print("3. Statistic of our network")
        print("4. Visualize all our routes")
        print("5. Query route detail")
        print("6. Find shortest routes")
        print("7. Exit")
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
            QueryRoute()
        elif(line == "6\n"):
            findPath()
        elif(line == "7\n"):
            exit()
        else:
            print("Please enter valid number")
def findPath():
    while(True):
        print "Please enter the code of the departing city:"
        print "For back to main menu enter b"
        line = readFromStdin()
        if(line == "b"):
            return 
        if(routing.metros.has_key(line) == False):
            print "Code does not exist!"
            continue
        dep = line
        print "Please enter the code of arriving city:"
        line = readFromStdin()
        if(routing.metros.has_key(line) == False):
            print "Code does not exist!"
            continue
        des = line
        distance = routing.findPath(dep, des)
        if(distance == 0):
            print "Route does not exist!"
        else:
            print "Distance: %d"%distance
def QueryRoute():
    while(True):
        print "Please enter the sequence of codes of cities in the route, end with 'END'"
        print "For back to main menu enter b"
        list = []
        current = readFromStdin()
        if(current == "b"):
            return
        if(routing.metros.has_key(current) == False):
            print "Code does not exist!"
            continue
        list.append(current)
        line = readFromStdin()
        while(line != "END"):
            if(current == "b"):
                return
            list.append(line)
            line = readFromStdin()
        if(len(list) == 1):
            print "Not enough cities to form a route! Please enter again."
            continue
        data = routing.getRouteData(list)
        if(len(data) == 0):
            continue
        print "Total distance:"
        print data[0]
        print "Total cost:"
        print data[1]
        print "Total time:"
        print data[2]
def ListAllCities():
    for city in routing.getCities():
        print routing.getCities()[city]._dict_["name"]

def readFromStdin():
    line = sys.stdin.readline()
    line = line[:-1]
    return line

def Query():
    while(True):
        print("Enter the code of city you would like to query:")
        print("Back to main menu, enter b")
        line = readFromStdin()
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
