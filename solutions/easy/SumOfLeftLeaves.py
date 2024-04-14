from typing import Optional

from node.TreeNode import TreeNode


class SumOfLeftLeaves:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        def check(node: TreeNode, is_left: bool) -> int:
            if not node:
                return 0
            if is_left and not node.left and not node.right:
                return node.val
            return check(node.left, True) + check(node.right, False)
        return check(root, False)


