from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        result = 0

        queue = deque()
        queue.append((root, float('-inf')))
        while queue:
            node, parent_max = queue.popleft()
            if node.val >= parent_max:
                result += 1
            
            parent_max = max(parent_max, node.val)
            if node.left:
                queue.append((node.left, parent_max))
            
            if node.right:
                queue.append((node.right, parent_max))
            
        return result