
import unittest
from RoutingGraph import RoutingGraph


class Test(unittest.TestCase):


    def setUp(self):
        routing = RoutingGraph()
        routing.load()

    def tearDown(self):
        pass


    def testNAme(self):
        pass


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()