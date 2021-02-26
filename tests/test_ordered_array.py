import unittest
import random

from ordered_array import OrderedArray


class TestOrderedArraySort(unittest.TestCase):
    # [1, 2, 3, 4, 5, 6, 7, 8, 9]


    def test_sort_correct(self):
        array = [1, 5, 7, 9, 2, 4, 3, 6, 8]
        expected = [1, 2, 3, 4, 5, 6, 7, 8, 9]

        ordered = OrderedArray(array)

        self.assertEqual(ordered.array, expected)
    
    
    def test_sort_length(self):
        array = [1, 5, 7, 9, 2, 4, 3, 6, 8]
        expected = len(array)

        ordered = OrderedArray(array)

        self.assertEqual(len(ordered.array), expected)


class TestOrderedArrayBinarySearch(unittest.TestCase):
    # [1, 2, 3, 4, 5, 6, 7, 8, 9]


    def test_binary_search_invalid(self):
        array = [1, 5, 7, 9, 2, 4, 3, 6, 8]
        expected = -1

        ordered = OrderedArray(array)

        self.assertEqual(ordered.binary_search(100), expected)
        self.assertEqual(ordered.binary_search(0), expected)
    
    
    def test_binary_search_correct(self):
        array = [1, 5, 7, 9, 2, 4, 3, 6, 8]

        ordered = OrderedArray(array)

        self.assertEqual(ordered.binary_search(5), 4)
        self.assertEqual(ordered.binary_search(9), 8)
        self.assertEqual(ordered.binary_search(1), 0)
        self.assertEqual(ordered.binary_search(3), 2)

    def test_binary_search_steps(self):
        array = [1, 5, 7, 9, 2, 4, 3, 6, 8]
        
        ordered = OrderedArray(array)

        self.assertEqual(ordered.binary_search(5, return_steps=True), 1)
        self.assertEqual(ordered.binary_search(9, return_steps=True), 5)
        self.assertEqual(ordered.binary_search(1, return_steps=True), 5)
