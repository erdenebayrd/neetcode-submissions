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
        return pattern in text