import unittest
from longest import get_longest_arr_string

class TestLongestStringFunction(unittest.TestCase):

    def test_longest(self):
        input_array = ['Roma', 'Kiev', 'Beijing', 'Barcelona', 'Omsk']
        result = get_longest_arr_string(input_array)
        self.assertEqual(result, 'Barcelona')

    def test_longest(self):
        input_array = ['Barcelona', 'Roma', 'Kiev', 'Beijing', 'Omsk']
        result = get_longest_arr_string(input_array)
        self.assertEqual(result, 'Barcelona')

    def test_longest(self):
        input_array = ['Roma', 'Kiev', 'Beijing', 'Omsk', 'Barcelona']
        result = get_longest_arr_string(input_array)
        self.assertEqual(result, 'Barcelona')
   
    def test_longest(self):
        input_array = ['Roma', 'Kiev', 'Omsk']
        result = get_longest_arr_string(input_array)
        self.assertEqual(result, 'Roma')

    def test_longest(self):
        input_array = ['Roma']
        result = get_longest_arr_string(input_array)
        self.assertEqual(result, 'Roma')


if __name__ == '__main__':
    unittest.main()
    