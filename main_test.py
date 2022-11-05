from pkgutil import get_data
import unittest
from main import *

class  TestMain(unittest.TestCase):

    def  test_get_data(self):
        filename = 'test.csv'
        result = [{'a'}, {'b','c'}, {'d','c','e'}, {'a','b','d','c'}, {'e'}]
        self.assertEqual(get_data(filename), result)
    

    def test_get_total_items(self):
        dataset = [{'a'}, {'d','c','e'}, {'a','b','d','c'}, {'e'}]
        self.assertEqual(get_total_items(dataset), 9)

    def test_get_unique_items(self):
        data = [{'a'}, {'d','c','e'}, {'a','b','d','c'}, {'e'}]
        self.assertEqual(get_unique_items(data), {'a', 'b', 'c', 'd', 'e'})

    def test_count_items(self):
        data = data = [{'a'}, {'d','c','e'}, {'a','b','d','c'}, {'e'}]
        self.assertEqual(count_items({'a'}, data), 2)
        self.assertEqual(count_items({'d','c'}, data), 2)
        self.assertEqual(count_items({'f'}, data), 0)



if __name__ == 'main':
    unittest.main()