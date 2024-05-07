import unittest
import time
import sys
from dz63function import factorial


class TestFactorial(unittest.TestCase):
    def test_pos_int(self):
        self.assertEqual(factorial(5), 120)

    def test_zero(self):
        self.assertEqual(factorial(0), 1)

    def test_neg_inp(self):
        with self.assertRaises(ValueError):
            factorial(-1)

    def test_large_inp(self):
        with self.assertRaises(ValueError):
            factorial(sys.maxsize)

    def test_float_inp(self):
        with self.assertRaises(TypeError):
            factorial(5.5)

    def test_string_inp(self):
        with self.assertRaises(TypeError):
            factorial("Test")

    def test_performance(self):
        begint = time.time()
        factorial(1000)
        endt = time.time()
        execution_time = endt - begint
        print(f"Время затраченное на тесты: {execution_time} сек.")
