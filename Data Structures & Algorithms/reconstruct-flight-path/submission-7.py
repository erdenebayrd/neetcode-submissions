class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = {}
        for source, target in sorted(tickets, reverse=True):
            if source not in adj:
                adj[source] = []
            adj[source].append(target)
        
        path = []
        def dfs(node: str) -> None:
            while node in adj and adj[node]:
                neighbor = adj[node].pop()
                dfs(neighbor)
            path.append(node)
        
        dfs("JFK")
        return path[::-1]