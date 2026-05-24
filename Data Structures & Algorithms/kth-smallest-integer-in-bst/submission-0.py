from functools import lru_cache

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    @lru_cache(None)
    def get_size(self, node: Optional[TreeNode]) -> int:
        if not node:
            return 0
        count = 1
        count += self.get_size(node.left)
        count += self.get_size(node.right)
        return count

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        left_size = self.get_size(root.left)
        right_size = self.get_size(root.right)
        if left_size >= k:
            return self.kthSmallest(root.left, k)
        elif left_size + 1 == k:
            return root.val
        else:
            return self.kthSmallest(root.right, k - left_size - 1)
