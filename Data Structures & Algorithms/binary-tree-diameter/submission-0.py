# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from typing import Tuple

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def dfs(root) -> Tuple[int, int]: # first value is distance between root and farthest node, second value is a diameter through this node
            if not root:
                return (0, 0)
            left_distance, left_diameter = dfs(root.left)
            right_distance, right_diameter = dfs(root.right)
            distance = max(left_distance, right_distance) + 1
            diameter = max(left_diameter, right_diameter)
            diameter = max(diameter, left_distance + right_distance + 1)
            return (distance, diameter)
        
        _, diameter = dfs(root)
        return diameter - 1