from collections import deque

class Solution:
    def canFinish(self, num_courses: int, prerequisites: List[List[int]]) -> bool:
        # time: O(num_courses + len(prerequisites)) -> O(V + E) V is a total number of vertices & E is total number of edges in the graph
        # space: O(num_courses) -> O(V)
        # method: Kahn algo

        indegree = [0] * num_courses
        graph = {}
        for a, b in prerequisites:
            if b not in graph:
                graph[b] = []
            graph[b].append(a)
            indegree[a] += 1
        
        queue = deque()
        for node in range(num_courses):
            if indegree[node] == 0:
                queue.append(node)
        
        while queue:
            node = queue.popleft()
            if node not in graph:
                continue

            for neighbor in graph[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0: # visited
                    queue.append(neighbor)
        
        return max(indegree) == 0