from collections import deque

class Solution:
    def findOrder(self, num_courses: int, prerequisites: List[List[int]]) -> List[int]:
        # time: O(V + E)
        # space: O(V)
        # method: Kahn's algo

        indegree = [0] * num_courses
        graph = [[] for _ in range(num_courses)]
        for v, u in prerequisites:
            graph[u].append(v)
            indegree[v] += 1
        
        order = []
        queue = deque()
        for node in range(num_courses):
            if indegree[node] == 0:
                queue.append(node)

        while queue:
            node = queue.popleft()
            order.append(node)
            for neighbor in graph[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
        
        if max(indegree) > 0:
            order = []
        return order