# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        while root:
            if root.val == p.val or root.val == q.val or p.val < root.val < q.val or q.val < root.val < p.val:
                return root
            if q.val < root.val and p.val < root.val:
                root = root.left
            else:
                root = root.right
        