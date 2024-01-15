import unittest
from size import size

class TestSizeFunction(unittest.TestCase):

    def test_valid_size(self):
        input_size = 0
        result = size(input_size)
        expected_value = '0 byte'
        self.assertEqual(result, expected_value)

    def test_valid_size(self):
        input_size = 1
        result = size(input_size)
        expected_value = '1 byte'
        self.assertEqual(result, expected_value)

    def test_valid_size(self):
        input_size = 12
        result = size(input_size)
        expected_value = '12 byte'
        self.assertEqual(result, expected_value)

    def test_valid_size(self):
        input_size = 123
        result = size(input_size)
        expected_value = '123 byte'
        self.assertEqual(result, expected_value)

    def test_valid_size(self):
        input_size = 1234
        result = size(input_size)
        expected_value = '1 kb'
        self.assertEqual(result, expected_value)

    def test_valid_size(self):
        input_size = 12345
        result = size(input_size)
        expected_value = '12 kb'
        self.assertEqual(result, expected_value)

    def test_valid_size(self):
        input_size = 123456
        result = size(input_size)
        expected_value = '123 kb'
        self.assertEqual(result, expected_value)

    def test_valid_size(self):
        input_size = 1234567
        result = size(input_size)
        expected_value = '1 mb'
        self.assertEqual(result, expected_value)

    def test_valid_size(self):
        input_size = 12345678
        result = size(input_size)
        expected_value = '12 mb'
        self.assertEqual(result, expected_value)

    def test_valid_size(self):
        input_size = 123456789
        result = size(input_size)
        expected_value = '123 mb'
        self.assertEqual(result, expected_value)

    def test_valid_size(self):
        input_size = 1234567890
        result = size(input_size)
        expected_value = '1 gb'
        self.assertEqual(result, expected_value)

if __name__ == '__main__':
    unittest.main()
    