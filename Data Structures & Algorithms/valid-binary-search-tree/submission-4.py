from typing import Tuple

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def is_valid(node: Optional[TreeNode], min_value: float, max_value: float) -> bool:
            if not node:
                return True
            
            if not (min_value < node.val < max_value):
                return False
            
            return is_valid(node.left, min_value, node.val) and is_valid(node.right, node.val, max_value)
        
        return is_valid(root, float('-inf'), float('inf'))