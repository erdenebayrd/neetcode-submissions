class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = {}
        for source, target in sorted(tickets, reverse=True):
            if source not in adj:
                adj[source] = []
            adj[source].append(target)
        
        path = []
        stack = ["JFK"]

        while stack:
            node = stack[-1]
            if node not in adj or not adj[node]:
                stack.pop()
                path.append(node)
            else:
                neighbor = adj[node].pop()
                stack.append(neighbor)
        return path[::-1]