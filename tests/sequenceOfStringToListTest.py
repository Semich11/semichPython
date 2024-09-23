import unittest
from sequenceOfStringToList import sequenceOfStringToList


class MyTestCase(unittest.TestCase):
    def test_For_expected_output(self):
        sequenceOfStringToList()
        self.assertEqual("['34', '67', '55', '33', '12', '98']('34', '67', '55', '33', '12', '98')", sequenceOfStringToList())  # add assertion here


if __name__ == '__main__':
    unittest.main()
