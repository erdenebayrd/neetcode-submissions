from functools import lru_cache
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        @lru_cache(None)
        def get_height(node: Optional[TreeNode]) -> int:
            if not node:
                return 0
            return max(get_height(node.left), get_height(node.right)) + 1
        
        left_height = get_height(root.left)
        right_height = get_height(root.right)
        if abs(left_height - right_height) > 1:
            return False

        return self.isBalanced(root.left) & self.isBalanced(root.right)
            