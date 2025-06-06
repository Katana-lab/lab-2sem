import unittest
from src.boyer_moore import boyer_moore_search


class TestBoyerMooreSearch(unittest.TestCase):
    def test_basic_match(self):
        self.assertEqual(boyer_moore_search("abracadabra", "abra"), [0, 7])

    def test_no_match(self):
        self.assertEqual(boyer_moore_search("hello world", "python"), [])

    def test_multiple_matches(self):
        self.assertEqual(boyer_moore_search("aaaaaa", "aa"), [0, 1, 2, 3, 4])

    def test_case_sensitive(self):
        self.assertEqual(boyer_moore_search("AbcabcABC", "abc"), [3])

    def test_empty_needle(self):
        self.assertEqual(boyer_moore_search("abc", ""), [])

    def test_empty_haystack(self):
        self.assertEqual(boyer_moore_search("", "abc"), [])

    def test_needle_longer_than_haystack(self):
        self.assertEqual(boyer_moore_search("short", "muchlonger"), [])


if __name__ == "__main__":
    unittest.main()
