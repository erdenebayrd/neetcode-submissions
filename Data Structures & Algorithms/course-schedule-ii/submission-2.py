from collections import deque

class Solution:
    def findOrder(self, num_courses: int, prerequisites: List[List[int]]) -> List[int]:
        # time: O(V + E)
        # space: O(V)
        # method: DFS
        order = []        
        visited = [0] * num_courses
        graph = [[] for _ in range(num_courses)]

        for a, b in prerequisites:
            graph[b].append(a)
        
        def has_cycle(node: int) -> bool:
            if visited[node] == 1:
                return True
            
            if visited[node] == 2:
                return False

            visited[node] = 1
            for neighbor in graph[node]:
                if has_cycle(neighbor):
                    return True
            
            visited[node] = 2
            order.append(node)
            return False

        for node in range(num_courses):
            if visited[node] == 0 and has_cycle(node):
                return []

        return order[::-1]