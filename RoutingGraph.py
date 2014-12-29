import json
import sys
from _mysql import NULL
from _heapq import heappush

class RoutingGraph:
    def __init__(self):
        self.metros = {}
        self.routes = {}
    def load(self):
        json_data = open('map_data.json')
        data = json.load(json_data)
        for city in data["metros"]:
            metro = City(
                         name =  city["name"],
                         country =  city["country"],
                         continent = city["continent"],
                         timezone = city["timezone"],
                         coordinates = city["coordinates"],
                         population = city["population"],
                         region = city["region"],
                         adj = {}
                         )        
            self.addCity(city["code"], metro)
        for route in data["routes"]:
            self.addRoute(route["ports"], route["distance"])
        json_data.close()
    def addCity(self, code, city):
        self.metros[code] = city
    def addRoute(self, ports, distance):
        port = Port(ports[0], ports[1])
        self.routes[port] = distance
        self.metros[ports[0]]._dict_["adj"][ports[1]] = distance
        self.metros[ports[1]]._dict_["adj"][ports[0]] = distance
    def getCities(self):
        return self.metros
    def getCityInfo(self, code):
        if(self.metros.has_key(code) == False):
            return NULL
        return self.metros[code]
    def findPath(self, dep, des):
        dist = {}
        previous = {}
        visited = []
        find = False
        dist[dep] = 0
        for code, city  in self.metros.items():
            if(code != dep):
                dist[code] = sys.maxint - 1
            visited.append(code)
        dist[des] = sys.maxint
        while(len(visited) != 0):
            minkey = min(visited, key = lambda(item) : dist[item])
            print minkey
            print dist[minkey]
            if(minkey == des):
                find = True
                break
            visited.remove(minkey)
            for city, distance in self.metros[minkey]._dict_["adj"].items():
                alt = dist[minkey] + distance
                if(alt < dist[city]):
                    dist[city] = alt
                    previous[city] = minkey
        if(find == False):
            return 0
        total = 0
        current = des
        while(previous.has_key(current)):
            distance = self.metros[previous[current]]._dict_["adj"][current]
            total +=distance
            current = previous[current]
        return total
    def getFlightStatistic(self):
        mini= sys.maxint
        maxi = 0
        minPort = Port("0", "0")
        maxPort  = Port("0", "0")
        totaldistance = 0  
        for ports, distance in self.routes.items():
            totaldistance+=distance
            if(distance < mini):
                mini = distance
                minPort = ports
            if(distance > maxi):
                maxi = distance
                maxPort = ports
        returnlist = []
        returnlist.append({minPort: maxi})
        returnlist.append({maxPort: mini})
        returnlist.append(totaldistance/len(self.routes))
        return returnlist
    def getCityStatistic(self):
        mini = sys.maxint
        maxi = 0
        minCity = City()
        maxCity = City()
        maxConnect = 0
        maxConnectCity = []
        totalSize = 0
        continents = {}
        for code, city in self.metros.items():
            if(continents.has_key(city._dict_["continent"]) == False):
                continents[city._dict_["continent"]] = Continent()
            continents[city._dict_["continent"]].cities.append(city)
            connection = len(city._dict_["adj"])
            if(connection > maxConnect):
                maxConnectCity = []
                maxConnectCity.append(city)
            elif(connection == maxConnect):
                maxConnectCity.append(city)
            size = city._dict_["population"]
            totalSize += size
            if(size < mini):
                mini = size
                minCity = city
            if(size > maxi):
                maxi = size
                maxCity = city
        returnlist = []
        returnlist.append(maxCity)
        returnlist.append(minCity)
        returnlist.append(totalSize/len(self.metros))
        returnlist.append(maxConnectCity)
        returnlist.append(continents)
        return returnlist
    def removeRoute(self, dep, des):
        for ports, distance in self.routes.items():
            if(ports.dep == dep and ports.des == des):
                self.routes.pop(ports)
                return True
        self.metros[dep]._dict_["adj"].pop(des)
        self.metros[des]._dict_["adj"].pop(dep)
        return False
    def getRouteData(self, list):
        distanceList = []
        returnList = []
        totalDistance = 0;
        current = list[0]
        find = False
        if(self.metros.has_key(current) == False):
            print "Start city does not exist!"
            return returnList
        for i in range(1, len(list)):
            for port, distance in self.routes.items():
                if(port.dep == current and port.des == list[i]):
                    distanceList.append(distance)
                    totalDistance += distance
                    current = list[i]
                    find = True
                    break
            if(find == False):
                print "Not a valid route!"
                return returnList
        returnList.append(totalDistance)
        returnList.append(self.calculateCost(distanceList))
        returnList.append(self.calculateTime(distanceList))
        return returnList
    def calculateCost(self, list):
        totalCost = 0
        constant = 0.35
        for i in range(len(list)):
            totalCost += constant*list[i]
            constant -= 0.05
            if(constant == 0):
                break
        return totalCost
    def calculateTime(self, list):
        return 1000
class City:
    def __init__(self, **arg):
        self._dict_ = dict(arg)
class Port:
    def __init__(self, dep, des):
        self.dep = dep
        self.des = des
class Continent:
    def __init__(self):
        self.cities = []
