import unittest

from queue import Queue  # pylint: disable=import-error


class TestQueue(unittest.TestCase):

    def setUp(self):
        self.queue = Queue()
        self.queue.__items__ = ["apples", "oranges", "bananas"]
    
    def test_dequeue(self):
        expected_dequeued = "apples"
        expected_items = ["oranges", "bananas"]

        self.assertEqual(self.queue.dequeue(), expected_dequeued)  # pylint: disable=maybe-no-member
        self.assertEqual(self.queue.__items__, expected_items)
    
    def test_enqueue(self):
        expected_items = ["apples", "oranges", "bananas", "grapefruit"]

        self.queue.enqueue("grapefruit")  # pylint: disable=maybe-no-member

        self.assertEqual(self.queue.__items__, expected_items)

    def test_read(self):
        expected_read = "apples"
        expected_items = ["apples", "oranges", "bananas"]

        self.assertEqual(self.queue.read(), expected_read)  # pylint: disable=maybe-no-member
        self.assertEqual(self.queue.__items__, expected_items)
