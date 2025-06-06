import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from lab6 import max_experience

class TestCareer(unittest.TestCase):
    def test_example1(self):
        levels = [
            [4],
            [3, 1],
            [2, 1, 5],
            [1, 3, 2, 1]
        ]
        self.assertEqual(max_experience(levels), 12)

    def test_example2(self):
        levels = [
            [9999]
        ]
        self.assertEqual(max_experience(levels), 9999)

    def test_example3(self):
        levels = [
            [0],
            [1, 1],
            [0, 0, 0],
            [1, 1, 1, 1],
            [0, 1, 0, 1, 0]
        ]
        self.assertEqual(max_experience(levels), 3)

    def test_single_zero(self):
        levels = [
            [0]
        ]
        self.assertEqual(max_experience(levels), 0)

    def test_large_simple(self):
        levels = [list(range(1, i + 2)) for i in range(1000)]
        expected = sum(i + 1 for i in range(1000))
        self.assertEqual(max_experience(levels), expected)

if __name__ == '__main__':
    unittest.main()
