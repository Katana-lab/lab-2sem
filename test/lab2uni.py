import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from lab2 import min_time_to_paint

class TestPainting(unittest.TestCase):
    def test_example_case(self):
        K = 10
        T = 5
        L = [10, 15, 10, 5, 10, 15, 20, 20, 15, 20]
        self.assertEqual(min_time_to_paint(K, T, L), 100)
    
    def test_single_painter(self):
        K = 1
        T = 2
        L = [5, 10, 15]
        self.assertEqual(min_time_to_paint(K, T, L), 60)
    
    def test_multiple_painters(self):
        K = 2
        T = 3
        L = [10, 20, 30, 40]
        self.assertEqual(min_time_to_paint(K, T, L), 180)
    
    def test_equal_shields_and_painters(self):
        K = 4
        T = 1
        L = [10, 20, 30, 40]
        self.assertEqual(min_time_to_paint(K, T, L), 40)
    
    def test_large_numbers(self):
        K = 3
        T = 10
        L = [100, 200, 300, 400, 500]
        self.assertEqual(min_time_to_paint(K, T, L), 6000)

if __name__ == "__main__":
    unittest.main()
