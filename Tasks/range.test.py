import unittest
from range import get_range

class TestRangeFunction(unittest.TestCase):

    def test_valid_range(self):
        Range = (10, 15)
        result = get_range(Range)
        self.assertEqual(result, [10, 11, 12, 13, 14, 15])

    def test_empty_range(self):
        Range = (-2, 2)
        result = get_range(Range)
        self.assertEqual(result, [-2, -1, 0, 1, 2])

    def test_single_value_range(self):
        Range = (2, -2)
        result = get_range(Range)
        self.assertEqual(result, [])

    def test_negative_range(self):
        Range = (2, 2)
        result = get_range(Range)
        self.assertEqual(result, [2])

    def test_invalid_range(self):
        Range = (0, 0)
        result = get_range(Range)
        self.assertEqual(result, [0])

if __name__ == '__main__':
    unittest.main()
    