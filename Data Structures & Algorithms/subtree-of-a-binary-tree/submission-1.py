# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def serialize(node: Optional[TreeNode]) -> str:
            if not node:
                return "#"
            return f"^{node.val},{serialize(node.left)},{serialize(node.right)}"
        
        text = serialize(root)
        pattern = serialize(subRoot)
        
        text = pattern + "$" + text
        n = len(text)
        z_value = [0] * n
        z_value[0] = n

        left = right = -1
        for i in range(1, n):
            if i < right:
                z_value[i] = min(z_value[i - left], right - i + 1)
            
            while i + z_value[i] < n and text[z_value[i]] == text[i + z_value[i]]:
                z_value[i] += 1
            
            if i + z_value[i] > right:
                left = i
                right = i + z_value[i] - 1
        
            if z_value[i] == len(pattern):
                return True
        return False

