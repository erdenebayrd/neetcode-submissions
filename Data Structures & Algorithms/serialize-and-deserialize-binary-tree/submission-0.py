# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        stack = [root]
        result = []
        while stack:
            node = stack.pop()
            if node:
                result.append(str(node.val))
                stack.append(node.right)
                stack.append(node.left)
            else:
                result.append("#")
        return ",".join(result)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        arr = data.split(",")
        if arr[0] == "#":
            return None
        root = TreeNode(int(arr[0]))
        stack = [(root, "right"), (root, "left")]
        for token in arr[1:]:
            parent, side = stack.pop()
            if token == "#": # null
                continue
            current_node = TreeNode(int(token))
            if side == "left":
                parent.left = current_node
            else:
                parent.right = current_node
            stack.append((current_node, "right"))
            stack.append((current_node, "left"))
        return root
            