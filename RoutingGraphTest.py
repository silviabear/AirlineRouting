
import unittest
from RoutingGraph import RoutingGraph


class Test(unittest.TestCase):
    
    def setUp(self):
        self.routing = RoutingGraph()
        self.routing.load()
    def tearDown(self):
        pass
    def testFindPath(self):
        distance = self.routing.findPath("BOG", "SAO")
        self.assertEquals(distance, 4323)
        print "-----------------------"
        distance = self.routing.findPath("LAX", "SAO")
        self.assertEquals(distance, 9980)
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()