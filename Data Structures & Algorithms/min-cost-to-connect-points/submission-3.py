from collections import deque

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # time: O(N ^ 2)
        # space: O(N ^ 2)
        # method: Prim optimized
        inf = float('inf')
        n = len(points)
        dist = [inf] * n
        dist[0] = 0
        queue = deque([0])
        visited = set()
        result = 0
        while queue and len(visited) < n:
            node = queue.popleft()
            result += dist[node]
            min_neighbor = -1
            min_distance = inf
            visited.add(node)
            for i in range(n):
                if i in visited:
                    continue
                current_distance = abs(points[node][0] - points[i][0]) + abs(points[node][1] - points[i][1])
                dist[i] = min(dist[i], current_distance)
                if min_distance > dist[i]:
                    min_distance = dist[i]
                    min_neighbor = i
            queue.append(min_neighbor)
        return result