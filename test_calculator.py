# https://github.com/mdaquila/lab10-MD-JD
# Partner 1: Matthew D'Aquila
# Partner 2: Joshua Dionne

import unittest
from calculator import *

# Partner 1: Matthew D'Aquila

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    def test_add(self):  # 3 assertions
        self.assertEqual(add(1, 2), 3)
        self.assertEqual(add(-5, 2), -3)
        self.assertEqual(add(0, 0), 0)

    def test_subtract(self):  # 3 assertions
        self.assertEqual(subtract(2, 2), 0)
        self.assertEqual(subtract(5, 2), 3)
        self.assertEqual(subtract(-5, -5), 0)
    # ##########################

    ######## Partner 1
    def test_multiply(self):
        self.assertEqual(mul(3, 4), 12)
        self.assertEqual(mul(-3, 4), -12)
        self.assertEqual(mul(0, 5), 0)

    def test_div(self):
        self.assertEqual(div(10, 2), 5)
        self.assertEqual(div(9, 3), 3)
        self.assertEqual(div(15, 3), 5)

        ######## Partner 2
    def test_divide_by_zero(self):  # 1 assertion
        with self.assertRaises(ZeroDivisionError):
            div(5, 0)

    def test_logarithm(self):  # 3 assertions
        self.assertEqual(logarithm(10, 10), 1)
        self.assertEqual(logarithm(5, 5), 1)
        self.assertEqual(logarithm(2, 2), 1)

    def test_log_invalid_base(self):  # 1 assertion
        with self.assertRaises(ValueError):
            logarithm(5, -5)
    # ##########################
    
    ######## Partner 1
    def test_log_invalid_argument(self):
        with self.assertRaises(ValueError):
            logarithm(10, -5)

    def test_hypotenuse(self):
        self.assertAlmostEqual(hypotenuse(3, 4), 5)
        self.assertAlmostEqual(hypotenuse(5, 12), 13)
        self.assertAlmostEqual(hypotenuse(8, 15), 17)

    def test_sqrt(self):
        with self.assertRaises(ValueError):
            square_root(-9)
        self.assertEqual(square_root(9), 3)
        self.assertEqual(square_root(16), 4)

if __name__ == "__main__":
    unittest.main()