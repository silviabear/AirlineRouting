from RoutingGraph import *
routing = RoutingGraph()
def start():
    routing.load()
    while(True):
        print("Please choose the type of your edition:")
        print("1. Remove a city")
        print("2. Remove a route")
        print("3. Add a city")
        print("4. Add a route")
        print("5. Edit an existing city")
        print("6. Quit")
        print("Please enter the number of items.")
        line = readFromStdin()
        if(line == "1"):
            removeCity()
        elif(line == "2"):
            removeRoute()
        elif(line == "3"):
            AddCity()
        elif(line == "4"):
            AddRoute()
        elif(line == "5"):
            EditCity()
        elif(line == "6"):
            exit()
        else:
            print "Please enter valid option."

def removeCity():
    while(True):
        print "Please enter the code of city you would like to delete:"
        print "Back to main menu enter b"
        line = readFromStdin()
        if(line == "b"):
            return
        else:
                if(routing.metros.has_key(line) == False):
                    print "Code does not exist!"
                    continue
                routing.metros.pop(line)
                print "Successfully delete!"
def removeRoute():
    while(True):
        print "Please enter the code of departure city of the route:"
        print "For back to main menu enter b"
        dep = readFromStdin()
        if(dep == "b"):
            return
        print "Please enter the code of destination of the route:"
        des = readFromStdin()
        if(routing.removeRoute(dep, des) == False):
            print "Route does not exist!"
        else:
            print "Successfully delete!"

def readFromStdin():
    name = sys.stdin.readline()
    name = name[:-1]
    return name

def readCityInformation(line):
    print "Please enter the following information"
    print "Name:"
    cname = readFromStdin()
    print "Country:"
    ccountry = readFromStdin()
    print "Continent:"
    ccontinent = readFromStdin()
    print "Timezone:"
    ctimezone = readFromStdin()
    print "Coordinates-first-Symbol:"
    c1 = readFromStdin()
    print "Coordinates-first-Value:"
    v1 = readFromStdin()
    print "Coordinates-second-Symbol:"
    c2 = readFromStdin()
    print "Coordinates-second-Value:"
    v2 = readFromStdin()
    ccoordinate = {}
    ccoordinate[c1] = v1
    ccoordinate[c2] = v2
    print "Population:"
    cpopulation = readFromStdin()
    print "Region:"
    cregion = readFromStdin()
    city = City(name=cname, 
        country=ccountry, 
        continent=ccontinent, 
        timezone=ctimezone, 
        coordinates=ccoordinate, 
        population=cpopulation, 
        region=cregion, 
        adj={})
    routing.addCity(line, city)

def AddCity():
    while(True):
        print "Please enter the code of city you  would like to add:"
        print "For back to main menu enter b"
        line = readFromStdin()
        if(line == "b"):
            return
        if(routing.metros.has_key(line) == True):
            print "Code already exist!"
            continue
        else:
            readCityInformation(line)
            print "Sucessfully add!"
def AddRoute():
    while(True):
        print "For back to main menu enter b"
        print "Please enter the code of departure city:"
        dep = readFromStdin()
        if(dep == "b"):
            return
        if(routing.metros.has_key(dep) == False):
            print "Code does not exist!"
            continue
        print "Please enter the code of arrival city:"
        des = readFromStdin()
        if(routing.metros.has_key(des) == False):
            print "Code does not exist!"
            continue
        print "Please enter the distance:"
        distance = readFromStdin()
        ports = [dep, des]
        routing.addRoute(ports, distance)
        print "Successfully add!"
def EditCity():
    while(True):
        print "Please enter the code of city you  would like to edit:"
        print "For back to main menu enter b"
        line = readFromStdin()
        if(line == "b"):
            return
        if(routing.metros.has_key(line) == False):
            print "Code does not exist!"
            continue
        else:
            readCityInformation(line)
            print "Sucessfully edit!"
if __name__ == '__main__':
    start()