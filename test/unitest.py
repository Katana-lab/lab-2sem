import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from lab1 import monoton

class TestMonoton(unittest.TestCase):
    def test_zrist(self):
        self.assertTrue(monoton([1, 2, 3, 4, 5]))
    
    def test_spad(self):
        self.assertTrue(monoton([5, 4, 3, 2, 1]))
    
    def test_ne_monoton(self):
        self.assertFalse(monoton([1, 2, 2, 3, 4, 5]))
    
    def test_rivni(self):
        self.assertTrue(monoton([3, 3, 3, 3]))
    
    def test_odunoki(self):
        self.assertTrue(monoton([7]))
    
    def test_pusti(self):
        self.assertTrue(monoton([]))

if __name__ == "__main__":
    unittest.main()
