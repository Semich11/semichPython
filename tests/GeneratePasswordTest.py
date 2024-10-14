import unittest

from password_generator import generate_password


class MyTestCase(unittest.TestCase):
    def test_that_length_is_16(self):
        self.assertEqual(16, len(generate_password(16)))  # add assertion here

if __name__ == '__main__':
    unittest.main()
