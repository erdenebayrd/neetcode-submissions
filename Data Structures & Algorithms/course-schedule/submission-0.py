from collections import deque

class Solution:
    def canFinish(self, num_courses: int, prerequisites: List[List[int]]) -> bool:
        # time: O(V + E)
        # space: O(V)
        # method: Kahn's algo (BFS)
        indegree = [0] * num_courses
        graph = {}

        for u, v in prerequisites:
            if v not in graph:
                graph[v] = []
            graph[v].append(u)
            indegree[u] += 1
        
        seen = set()
        queue = deque()
        for v in range(num_courses):
            if indegree[v] == 0:
                queue.append(v)
                seen.add(v)
        
        while queue:
            node = queue.popleft()
            if node not in graph:
                continue

            for neighbor in graph[node]:
                if neighbor in seen:
                    continue
                seen.add(neighbor)
                queue.append(neighbor)
        
        return len(seen) == num_courses