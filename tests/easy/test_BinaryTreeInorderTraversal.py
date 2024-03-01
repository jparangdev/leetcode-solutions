import unittest

from node.TreeNode import TreeNode
from solutions.easy.BinaryTreeInorderTraversal import BinaryTreeInorderTraversal


class TestBinaryTreeInorderTraversal(unittest.TestCase):
    def setUp(self):
        self.binary_tree_inorder_traversal = BinaryTreeInorderTraversal()

    def test_inorder_traversal(self):
        # creating instance of binary tree
        root = TreeNode(1)
        root.right = TreeNode(2)
        root.right.left = TreeNode(3)

        # invoking method on binary tree instance
        result = self.binary_tree_inorder_traversal.inorderTraversal(root)

        # asserting the result
        self.assertEqual(result, [1, 3, 2])


if __name__ == '__main__':
    unittest.main()
