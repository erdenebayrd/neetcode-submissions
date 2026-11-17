class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        tickets.sort()
        adj = {}
        for u, v in tickets:
            if u not in adj:
                adj[u] = []
            adj[u].append(v)
        
        result = ["JFK"]

        def dfs(node: str) -> bool:
            if len(result) - 1 == len(tickets):
                return True
            if node not in adj or not adj[node]:
                return False
            
            for i in range(len(adj[node])):
                neighbor = adj[node][i]
                if i > 0 and adj[node][i - 1] == neighbor:
                    continue
                result.append(neighbor)
                adj[node].pop(i)
                if dfs(neighbor):
                    return True
                result.pop()
                adj[node].insert(i, neighbor)
            return False
        
        dfs("JFK")
        return result