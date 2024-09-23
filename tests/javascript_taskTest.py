import unittest

from javascript_task import occurrence_count


class MyTestCase(unittest.TestCase):
    def test_that_occurrence_count_function_will_give_me_expected_result(self):
        self.assertEqual({4: 1, 5: 3, 6: 2, 7: 1}, occurrence_count([5,4,5,5,6,7,6]))
        # add assertion here
    def test_that_occurrence_count_function_will_give_me_expected_results(self):
        self.assertEqual({1: 2, 2: 2, 3: 1}, occurrence_count([1,1,2,3,2]))  # add assertion here

if __name__ == '__main__':
    unittest.main()
