import json
class RoutingGraph:
    def __init__(self):
        self.metros = {}
        self.routes = []
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
                         adj = []
                         )        
            self.addCity(city["code"], metro)
        for route in data["routes"]:
            self.addRoute(route["ports"], route["distance"])
        json_data.close()
    def addCity(self, code, city):
        self.metros[code] = city
    def addRoute(self, ports, distance):
        route = Route(ports = ports, distance = distance)
        self.routes.append(route)
        self.metros[ports[0]]._dict_["adj"].append(ports[1])
    def getCities(self):
        return self.metros
class City:
        def __init__(self, **arg):
            self._dict_ = dict(arg)
class Route:
        def __init__(self, **arg):
            self._dict_ = dict(arg)