import unittest

from Stack import Stack

class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.stack = Stack()
    # end

    def test_that_stack_is_empty(self):
        self.assertTrue(self.stack.empty())
    #end

    def test_push_an_item_to_the_stack(self):
        self.stack.push("g_string")
        self.assertFalse(self.stack.empty())
    #end

    def test_push_two_times(self):
        self.stack.push("g_string")
        self.stack.push("f_string")
        self.assertFalse(self.stack.empty())
    #end

    def test_pop(self):
        self.stack.push("g_string")
        self.assertTrue("g_string", self.stack.pop())
    #end

    def test_That_pop_throw_exception_if_array_is_empty(self):
        with self.assertRaises(IndexError):
            self.stack.pop()
    #end

    def test_when_push_twice_and_pop_one_that_stack_is_not_empty(self):
        self.stack.push("g_string")
        self.stack.push("f_string")
        self.stack.pop()
        self.assertFalse(self.stack.empty())
    #end

    def test_that_peek_method_will_return_f_string(self):
        self.stack.push("g_string")
        self.stack.push("f_string")
        self.assertEqual("f_string", self.stack.peek())
    #end

    def test_That_peek_throw_exception_if_array_is_empty(self):
        with self.assertRaises(IndexError):
            self.stack.peek()
    #end

    def test_search_method(self):
        self.stack.push("g_string")
        self.stack.push("f_string")
        self.assertEqual(1, self.stack.search('f_string'))
    #end

    def test_That_search_method_return_negative_1_if_the_element_is_not_found(self):
        self.stack.push("g_string")
        self.stack.push("f_string")
        self.assertEqual(-1, self.stack.search('d_string'))
    #end






if __name__ == '__main__':
    unittest.main()
