import unittest
from types_ import count_types

class TestCountTypesFunction(unittest.TestCase):

    def test_valid_types_count(self):
        l = [5, True, 'string', 7, 'hello']
        result = count_types(l)
        expected_dict = { 'int': 2, 'str': 2, 'bool': 1 }
        self.assertEqual(result, expected_dict)

    def test_valid_types_count(self):
        l = [True, True]
        result = count_types(l)
        expected_dict = { 'int': 0, 'str': 0, 'bool': 2 }
        self.assertEqual(result, expected_dict)

    def test_valid_types_count(self):
        l = []
        result = count_types(l)
        expected_dict = { 'int': 0, 'str': 0, 'bool': 0 }
        self.assertEqual(result, expected_dict)

    def test_valid_types_count(self):
        l = [100]
        result = count_types(l)
        expected_dict = { 'int': 1, 'str': 0, 'bool': 0 }
        self.assertEqual(result, expected_dict)

if __name__ == '__main__':
    unittest.main()
    