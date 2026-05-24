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

        def dfs(root: TreeNode) -> Tuple[bool, int, int]: # is_valid, min value and max value of subtree at root
            
            min_value = max_value = root.val
            if root.left:
                left_valid, left_min, left_max = dfs(root.left)
                if not left_valid or left_max >= root.val:
                    return (False, 0, 0)
                min_value = min(min_value, left_min)
                max_value = max(max_value, left_max)
            
            if root.right:
                right_valid, right_min, right_max = dfs(root.right)
                if not right_valid or root.val <= right_min:
                    return (False, 0, 0)
                min_value = min(min_value, right_min)
                max_value = max(max_value, right_max)

            return (True, min_value, max_value)
        
        is_valid, _, _ = dfs(root)
        return is_valid

            
