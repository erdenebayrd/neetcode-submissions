from collections import defaultdict, deque

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # time: O(N log N)
        # space: O(N)
        # method: DFS

        graph = defaultdict(list)
        for source, target in tickets:
            graph[source].append(target)
        
        adj = defaultdict(deque)
        for node in graph:
            adj[node] = deque(sorted(graph[node]))
        
        result = []
        current = []
        def dfs(node: str) -> bool:
            nonlocal result
            if len(result) > 0:
                return True

            if len(current) == len(tickets):
                result = current[:]
                return True

            while len(adj[node]) > 0:
                neighbor = adj[node].popleft()
                current.append(neighbor)
                if dfs(neighbor):
                    return True
                current.pop()
                adj[node].append(neighbor) # added at right
        
        dfs("JFK")
        result = ["JFK"] + result
        return result


