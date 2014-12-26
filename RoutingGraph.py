import json
class RoutingGraph:
    def __init__(self):
        self.metros = {}
        self.routes = []
    def load(self, path):
        json_data = open('map_data.json')
        data = json.load(json_data)
        for city in data["metros"]:
            metro = City(
                         code = city["code"],
                         name =  city["name"],
                         country =  city["country"],
                         continent = city["continent"],
                         timezone = city["timezone"],
                         coordinates = city["coordinates"],
                         population = city["population"],
                         region = city["region"]
                         )        
            self.addCity(metro)
        for route in data["routes"]:
            self.addRoute(route["ports"], route["distance"])
        json_data.close()
    def addCity(self, city):
        self.metros[city] = []
    def addRoute(self, ports, distance):
        route = Route(ports = ports, distance = distance)
        self.routes.append(route)
        self.metros.get(ports[0]).append(ports[1])
class City:
        def __init__(self, **arg):
            self._dict_ = dict(arg)
        def connect(self, dest):
            self.adj.append(dest)
class Route:
        def __init__(self, **arg):
            self._dict_ = dict(arg)