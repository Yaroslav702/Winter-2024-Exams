import unittest
from month import get_month_number

class TestMonthNumberFunction(unittest.TestCase):

    def test_valid_month(self):
        month_name = 'january'
        result = get_month_number(month_name)
        self.assertEqual(result, 1)

    def test_valid_month(self):
        month_name = 'february'
        result = get_month_number(month_name)
        self.assertEqual(result, 2)

    def test_valid_month(self):
        month_name = 'feb'
        result = get_month_number(month_name)
        self.assertEqual(result, 2)

    def test_valid_month(self):
        month_name = 'February'
        result = get_month_number(month_name)
        self.assertEqual(result, 2)
        
    def test_valid_month(self):
        month_name = 'Feb'
        result = get_month_number(month_name)
        self.assertEqual(result, 2)

    def test_valid_month(self):
        month_name = 'abc'
        result = get_month_number(month_name)
        self.assertEqual(result, -1)

    def test_valid_month(self):
        month_name = ''
        result = get_month_number(month_name)
        self.assertEqual(result, -1)


if __name__ == '__main__':
    unittest.main()
    