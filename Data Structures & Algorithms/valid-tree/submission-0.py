class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # time: O(V + E)
        # space: O(V)
        # method: DFS cycle detection
        visited = [0] * n
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        def has_cycle(node: int, parent: int) -> bool:
            if visited[node] == 1:
                return True
            
            if visited[node] == 2:
                return False
            
            visited[node] = 1
            for neighbor in graph[node]:
                if neighbor == parent:
                    continue
                if has_cycle(neighbor, node):
                    return True
            
            visited[node] = 2
            return False
        
        if has_cycle(0, -1):
            return False

        return min(visited) == 2