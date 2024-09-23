import unittest

from functions import *


class MyTestCase(unittest.TestCase):
    def test_swap_string(self):
        self.assertEqual(swap_string("abc", "xyz"), "xyc abz")  # add assertion here


if __name__ == '__main__':
    unittest.main()
