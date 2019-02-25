import unittest
from math import gcd
from eratosthene import init_data, erastofen

class MyUnitTest(unittest.TestCase):
    def test_input(self):
        MyUnitTest.data = init_data()
        self.assertIsInstance(MyUnitTest.data, int)

    def test_erastofen(self):
        list = erastofen(init_data())
        self.assertFalse([True for item in list if gcd(item, 2) > 2])
