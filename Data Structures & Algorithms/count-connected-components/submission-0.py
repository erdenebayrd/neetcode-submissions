class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # time: O(V + E)
        # space: O(V)
        # method: DFS

        seen = set()
        count = 0
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        def visit(node: int) -> None:
            seen.add(node)
            for neighbor in graph[node]:
                if neighbor in seen:
                    continue
                visit(neighbor)

        for node in range(n):
            if node not in seen:
                visit(node)
                count += 1
        return count