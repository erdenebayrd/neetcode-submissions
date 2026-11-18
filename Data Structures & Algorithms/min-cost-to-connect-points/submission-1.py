from collections import deque
import heapq

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # time: O(N ^ 2 * log (N ^ 2))
        # space: O(N ^ 2)
        # method: Prim
        
        n = len(points)
        queue = deque()
        queue.append(0) # as index
        min_heap = []
        visited = set()
        result = 0

        def dist(i, j):
            return abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])

        while queue and len(visited) < n - 1:
            node = queue.popleft()
            visited.add(node)
            for i in range(n):
                if i in visited:
                    continue
                heapq.heappush(min_heap, (dist(i, node), i))
            
            while min_heap and min_heap[0][-1] in visited:
                heapq.heappop(min_heap)
            
            cost, next_node = heapq.heappop(min_heap)
            queue.append(next_node)
            result += cost
        return result