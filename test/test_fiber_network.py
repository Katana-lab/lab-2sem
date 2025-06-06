import unittest
import os
from src.fiber_network import minimum_cable_length

TEST_CSV_PATH = "test/test_data.csv"


class TestFiberNetwork(unittest.TestCase):
    def tearDown(self):
        if os.path.exists(TEST_CSV_PATH):
            os.remove(TEST_CSV_PATH)

    def write_test_csv(self, content):
        with open(TEST_CSV_PATH, "w", encoding="utf-8") as f:
            f.write(content)

    def test_connected_graph(self):
        self.write_test_csv("A,B,10\nB,C,15\nA,C,20")
        self.assertEqual(minimum_cable_length(TEST_CSV_PATH), 25)

    def test_disconnected_graph(self):
        self.write_test_csv("A,B,10\nC,D,15")
        self.assertEqual(minimum_cable_length(TEST_CSV_PATH), -1)

    def test_single_node(self):
        self.write_test_csv("A,A,0")
        self.assertEqual(minimum_cable_length(TEST_CSV_PATH), 0)

    def test_empty_file(self):
        self.write_test_csv("")
        self.assertEqual(minimum_cable_length(TEST_CSV_PATH), -1)


if __name__ == "__main__":
    unittest.main()
