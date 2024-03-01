from typing import Optional, List

from node.TreeNode import TreeNode


class BinaryTreeInorderTraversal:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        self.traverse(root, result)
        return result

    def traverse(self, node: Optional[TreeNode], result: List[int]):
        if node is None:
            return
        self.traverse(node.left, result)
        result.append(node.val)
        self.traverse(node.right, result)
