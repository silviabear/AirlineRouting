import json
import sys
from _mysql import NULL

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
    def getCities(self):
        return self.metros
    def getCityInfo(self, code):
        if(self.metros.has_key(code) == False):
            return NULL
        return self.metros[code]
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
        return False
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
