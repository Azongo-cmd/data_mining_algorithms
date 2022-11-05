from pkgutil import get_data
import unittest
from main import get_data

class  TestMain(unittest.TestCase):

    def  test_get_data(self):
        filename = 'test.csv'
        result = [['a'], ['b','c'], ['d','c','e'], ['a','b','d','c'], ['e']]
        self.assertEqual(get_data(filename), result)




if __name__ == 'main':
    unittest.main()