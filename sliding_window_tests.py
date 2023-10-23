# sliding window tests
# Name: Joshua Estrada
import unittest
from sliding_window import*

class TestHeap(unittest.TestCase):
    def test_substring(self):
        self.assertEqual(find_substring("hello", "hel"), 0)
        self.assertEqual(find_substring("mississippi", "issi"), 1)
        self.assertEqual(find_substring("abcdefg", "def"), 3)
        self.assertEqual(find_substring("", "def"), -1)

    def test_max_sum(self):
        self.assertEqual(max_sum([1, 2, 3, 4, 5, 6], 3), 15)
        self.assertEqual(max_sum([1, 2, 3, 4, 5, 2], 3), 12)
        self.assertEqual(max_sum([1, 2, 3], 3), 6)
        self.assertEqual(max_sum([1], 3), -1)

        self.assertEqual(max_sum_bruteforce([1, 2, 3, 4, 5, 6], 3), 15)
        self.assertEqual(max_sum_bruteforce([1, 2, 3, 4, 5, 2], 3), 12)
        self.assertEqual(max_sum_bruteforce([1, 2, 3], 3), 6)
        self.assertEqual(max_sum_bruteforce([1], 3), -1)
