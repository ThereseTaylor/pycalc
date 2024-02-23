import unittest
from calculator import add, subtract, multiply, divide

class TestCalculator(unittest.TestCase):

    def test_add(self):
        result = add(3, 7)
        self.assertEqual(result, 10)

    def test_subtract(self):
        result = subtract(10, 4)
        self.assertEqual(result, 6)

    def test_multiply(self):
        result = multiply(5, 3)
        self.assertEqual(result, 15)

    def test_divide(self):
        result = divide(8, 2)
        self.assertEqual(result, 4)

    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            divide(10, 0)

if __name__ == '__main__':
    unittest.main()
