import json
from _mysql import NULL
class RoutingGraph:
    def __init__(self):
        self.metros = {}
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
        self.metros[ports[0]]._dict_["adj"][ports[1]] = distance
    def getCities(self):
        return self.metros
    def getCityInfo(self, code):
        if(self.metros.has_key(code) == False):
            return NULL
        return self.metros[code]
class City:
        def __init__(self, **arg):
            self._dict_ = dict(arg)