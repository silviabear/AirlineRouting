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
        line = sys.stdin.readline()
        line = line[:-1]
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
        line = sys.stdin.readline()
        line = line[:-1]
        if(line == "b"):
            return
        else:
            if(routing.metros.has_key(line) == False):
                print "Code does not exist!"
            else:
                routing.metros.pop(line)
                print "Successful delete!"
def removeRoute():
    pass
def AddCity():
    pass
def AddRoute():
    pass
def EditCity():
    pass
if __name__ == '__main__':
    start()