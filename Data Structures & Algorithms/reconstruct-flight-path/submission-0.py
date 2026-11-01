from collections import deque

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # time: O(V log V) V length of tickets
        # space: O(V)
        # method: DFS
        graph = {}
        for u, v in tickets:
            if u not in graph:
                graph[u] = []
            graph[u].append(v)
        
        for node in graph:
            graph[node] = deque(sorted(graph[node]))
        
        source = "JFK"
        route = []
        def dfs(node: str) -> None:
            route.append(node)
            if node in graph and graph[node]:
                neighbor = graph[node].popleft()
                dfs(neighbor)
        
        dfs(source)
        return route