import unittest
from solutions.easy.SumOfLeftLeaves import SumOfLeftLeaves
from typing import Optional


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class TestSumOfLeftLeaves(unittest.TestCase):
    def setUp(self):
        self.solution = SumOfLeftLeaves()

    def test_sumOfLeftLeaves_given_example(self):
        root = TreeNode(3)
        root.left = TreeNode(9)
        root.right = TreeNode(20)
        root.right.left = TreeNode(15)
        root.right.right = TreeNode(7)
        self.assertEqual(self.solution.sumOfLeftLeaves(root), 24)

    def test_sumOfLeftLeaves_no_left_leaves(self):
        """
        In this case, the tree has no left leaves. Therefore, the output should be 0.
        """
        root = TreeNode(1)
        root.right = TreeNode(2)
        root.right.right = TreeNode(3)
        self.assertEqual(self.solution.sumOfLeftLeaves(root), 0)

    def test_sumOfLeftLeaves_single_node(self):
        """
        In this case, the tree has only one node. Therefore, the output should be 0 since single nodes 
        are not considered as left leaves.
        """
        root = TreeNode(1)
        self.assertEqual(self.solution.sumOfLeftLeaves(root), 0)

    def test_sumOfLeftLeaves_all_nodes_are_left_leaves(self):
        """
        In this case, the tree has all nodes as left leaves (excl root). Therefore, the output should 
        be the sum of all node values.
        """
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.left.left = TreeNode(3)
        self.assertEqual(self.solution.sumOfLeftLeaves(root), 3)

    def test_sumOfLeftLeaves_null(self):
        """
        Test case where the root node is None. The expected result is 0.
        """
        root = None
        self.assertEqual(self.solution.sumOfLeftLeaves(root), 0)


if __name__ == "__main__":
    unittest.main()
