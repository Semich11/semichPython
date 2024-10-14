import unittest

from Bike import Bike


class MyTestCase(unittest.TestCase):
    def test_that_new_bike_is_off(self):
        bike = Bike()
        self.assertEqual(False, bike.bike_is_on())  # add assertion here

    def test_that_bike_can_be_turned_on(self):
        bike = Bike()
        bike.on_bike()
        self.assertEqual(True, bike.bike_is_on())

if __name__ == '__main__':
    unittest.main()
