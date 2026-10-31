"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # time: O(V + E)
        # space: O(V + E)
        # method: BFS + bridge
        if not node:
            return None

        bridge = {}

        queue = deque()
        queue.append(node)
        bridge[node] = Node(node.val)

        while queue:
            current = queue.popleft()
            for neighbor in current.neighbors:
                if neighbor not in bridge:
                    bridge[neighbor] = Node(val=neighbor.val)
                    queue.append(neighbor)
                bridge[current].neighbors.append(bridge[neighbor])
        
        return bridge[node]
        