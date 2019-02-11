import unittest
from string_sep_test import init_data, separate


class MyUnitTest(unittest.TestCase):
    def test_input(self):
        data = init_data()
        self.assertTrue(data[0].isprintable() and data[1].isprintable())

    def test_separator(self):
        set_o = separate(*init_data())
        self.assertTrue([elem for elem in set_o if elem[0].isdigit])