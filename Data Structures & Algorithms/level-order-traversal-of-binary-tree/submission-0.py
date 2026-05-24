# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.levels = defaultdict(list)
        
        def dfs(node: Optional[TreeNode], current_level: int) -> None:
            if not node:
                return
            self.levels[current_level].append(node.val)
            dfs(node.left, current_level + 1)
            dfs(node.right, current_level + 1)
        
        dfs(root, 0)
        result = []
        for level in self.levels:
            result.append(self.levels[level])
        return result