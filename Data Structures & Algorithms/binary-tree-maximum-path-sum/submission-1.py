from typing import Tuple

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        def dfs(node: Optional[TreeNode]) -> Tuple[int, int]: # max_sum, max_path_sum
            if not node:
                return (0, float('-inf'))
            
            left_max_sum, left_max_path_sum = dfs(node.left)
            right_max_sum, right_max_path_sum = dfs(node.right)
            max_sum = max(left_max_sum, right_max_sum) + node.val
            max_sum = max(max_sum, 0)
            
            max_path_sum = max(left_max_path_sum, right_max_path_sum)
            max_path_sum = max(max_path_sum, left_max_sum + right_max_sum + node.val)

            return (max_sum, max_path_sum)

        _, max_path_sum = dfs(root)
        return max_path_sum