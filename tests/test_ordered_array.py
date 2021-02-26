import unittest

from ordered_array import OrderedArray


class TestOrderedArraySort(unittest.TestCase):
    # [1, 2, 3, 4, 5, 6, 7, 8, 9]
    array = [1, 5, 7, 9, 2, 4, 3, 6, 8]
    array_length = len(array)
    ordered = OrderedArray(array)

    def test_sort_correct(self):
        expected = [1, 2, 3, 4, 5, 6, 7, 8, 9]

        self.assertEqual(self.ordered.array, expected)
    
    
    def test_sort_length(self):
        expected = self.array_length

        self.assertEqual(len(self.ordered.array), expected)


class TestOrderedArrayBinarySearch(unittest.TestCase):
    # [1, 2, 3, 4, 5, 6, 7, 8, 9]
    array = [1, 5, 7, 9, 2, 4, 3, 6, 8]
    ordered = OrderedArray(array)


    def test_binary_search_invalid(self):
        expected = -1

        self.assertEqual(self.ordered.binary_search(100), expected)
        self.assertEqual(self.ordered.binary_search(0), expected)
    
    
    def test_binary_search_correct(self):
        self.assertEqual(self.ordered.binary_search(5), 4)
        self.assertEqual(self.ordered.binary_search(9), 8)
        self.assertEqual(self.ordered.binary_search(1), 0)
        self.assertEqual(self.ordered.binary_search(3), 2)

    def test_binary_search_steps(self):
        self.assertEqual(self.ordered.binary_search(5, return_steps=True), 1)
        self.assertEqual(self.ordered.binary_search(9, return_steps=True), 5)
        self.assertEqual(self.ordered.binary_search(1, return_steps=True), 5)
