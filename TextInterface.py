#! /usr/bin/python
from RoutingGraph import *
import sys

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
    pass
def Statistic():
    pass
if __name__ == '__main__':
    start()
