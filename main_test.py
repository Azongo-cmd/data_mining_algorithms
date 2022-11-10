from operator import sub
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
        self.assertEqual(get_total_items(dataset), 4)

    def test_get_unique_items(self):
        data = [{'a'}, {'d','c','e'}, {'a','b','d','c'}, {'e'}]
        self.assertEqual(get_unique_items(data), [{'e'}, {'b'}, {'d'}, {'a'}])

    def test_count_items(self):
        data = data = [{'a'}, {'d','c','e'}, {'a','b','d','c'}, {'e'}]
        self.assertEqual(count_items({'a'}, data), 2)
        self.assertEqual(count_items({'d','c'}, data), 2)
        self.assertEqual(count_items({'f'}, data), 0)
    
    def test_get_subset(self):
        item = {'a','b', 'c'}
        subsets = [{'a','b'}, {'a','c'}, {'b','c'}]
        #self.ass(get_subsets(item, 2), subsets)
    
    def test_is_all_subset_exist(self):
        subset1 = [{'a','b'}, {'a','c'}, {'b','c'}]
        subset2 = [{'a','b'}, {'a','c'}, {'b','e'}]
        candidate = [{'a','b'}, {'a','c'}, {'b','c'}, {'a','e'},{'c','e'}]
        self.assertEqual(is_all_subset_exist(candidate,subset1), True)
        self.assertEqual(is_all_subset_exist(candidate,subset2), False)



if __name__ == 'main':
    unittest.main()