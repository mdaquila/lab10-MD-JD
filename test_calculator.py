import unittest
from calculator import *

# Partner 1: Matthew D'Aquila

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    # def test_add(self): # 3 assertions
    #     fill in code

    # def test_subtract(self): # 3 assertions
    #     fill in code
    # ##########################

    ######## Partner 1
    def test_multiply(self):
        self.assertEqual(mul(3, 4), 12)
        self.assertEqual(mul(-3, 4), -12)
        self.assertEqual(mul(0, 5), 0)

    def test_divide(self):
        self.assertEqual(divide(10, 2), 5)
        self.assertEqual(divide(9, 3), 3)
        with self.assertRaises(ZeroDivisionError):
            divide(10, 0)

    ######## Partner 2
    # def test_divide_by_zero(self): # 1 assertion
    #     # call division function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     div(0, 5)
    #     fill in code

    # def test_logarithm(self): # 3 assertions
    #     fill in code

    # def test_log_invalid_base(self): # 1 assertion
    #     # use same technique from test_divide_by_zero
    #     fill in code
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