import unittest

from stack import Stack  # pylint: disable=import-error


class TestStack(unittest.TestCase):

    def setUp(self):
        self.stack = Stack()
        self.stack.__items__ = ["apples", "oranges", "bananas", "watermelon"]
    
    def test_push(self):
        expected = ["apples", "oranges", "bananas", "watermelon", "grapefruit"]

        self.stack.push("grapefruit")

        self.assertEqual(self.stack.__items__, expected)

    def test_read(self):
        expected_read = "watermelon"
        expected_items = ["apples", "oranges", "bananas", "watermelon"]

        self.assertEqual(self.stack.read(), expected_read)
        self.assertEqual(self.stack.__items__, expected_items)
    
    def test_pop(self):
        expected_pop = "watermelon"
        expected_items = ["apples", "oranges", "bananas"]

        self.assertEqual(self.stack.pop(), expected_pop)
        self.assertEqual(self.stack.__items__, expected_items)
