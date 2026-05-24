from typing import Tuple

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        def dfs(node: TreeNode) -> Tuple[bool, int]:
            left_max = float('-inf')
            right_max = float('inf')
            left_valid = True
            right_valid = True
            value = node.val
            if node.left:
                left_valid, left_max = dfs(node.left)
                value = max(left_max, value)
            if node.right:
                right_valid, right_max = dfs(node.right)
                value = max(right_max, value)

            is_valid = left_valid and right_valid and left_max < node.val < right_max
            return (is_valid, value)
        
        is_valid, _ = dfs(root)
        return is_valid
