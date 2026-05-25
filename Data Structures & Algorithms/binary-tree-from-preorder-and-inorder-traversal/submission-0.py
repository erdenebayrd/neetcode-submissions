# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        n = len(preorder)

        def build_tree(pre_left: int, pre_right: int, in_left: int, in_right: int) -> Optional[TreeNode]:
            if pre_left > pre_right or in_left > in_right:
                return None
            
            value = preorder[pre_left]
            in_index = -1
            for i in range(in_left, in_right + 1):
                if inorder[i] == value:
                    in_index = i
                    break
            node = TreeNode(preorder[pre_left])
            in_left_length = in_index - in_left
            node.left = build_tree(pre_left + 1, pre_left + in_left_length, in_left, in_index - 1)
            in_right_length = in_right - in_index
            node.right = build_tree(pre_left + in_left_length + 1, pre_right, in_index + 1, in_right)
            return node

        return build_tree(0, n - 1, 0, n - 1)
