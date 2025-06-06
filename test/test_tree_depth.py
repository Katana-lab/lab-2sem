import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from tree_depth import TreeNode, sum_of_depths


class TestSumOfDepths(unittest.TestCase):
    def test_example(self):
        # Приклад з умови
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(5)
        self.assertEqual(sum_of_depths(root), 6)

    def test_empty_tree(self):
        self.assertEqual(sum_of_depths(None), 0)

    def test_single_node(self):
        root = TreeNode(10)
        self.assertEqual(sum_of_depths(root), 0)

    def test_left_skewed_tree(self):
        # дерево: 1 -> 2 -> 3
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.left.left = TreeNode(3)
        # глибини: 0 + 1 + 2 = 3
        self.assertEqual(sum_of_depths(root), 3)

    def test_right_skewed_tree(self):
        # дерево: 1 -> 2 -> 3
        root = TreeNode(1)
        root.right = TreeNode(2)
        root.right.right = TreeNode(3)
        # глибини: 0 + 1 + 2 = 3
        self.assertEqual(sum_of_depths(root), 3)


if __name__ == "__main__":
    unittest.main()
