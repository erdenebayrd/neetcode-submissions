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

        while queue:
            current = queue.popleft()
            bridge[current] = Node(val=current.val)
            for neighbor in current.neighbors:
                if neighbor in bridge:
                    continue
                bridge[neighbor] = Node(val=neighbor.val)
                queue.append(neighbor)
        
        queue = deque()
        queue.append(node)

        seen = set()
        seen.add(node)
        while queue:
            current = queue.popleft()
            
            for neighbor in current.neighbors:
                bridge[current].neighbors.append(bridge[neighbor])
                if neighbor not in seen:
                    seen.add(neighbor)
                    queue.append(neighbor)

        return bridge[node]