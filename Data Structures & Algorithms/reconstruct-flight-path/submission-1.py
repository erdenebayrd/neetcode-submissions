from collections import defaultdict

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # time: O(N log N)
        # space: O(N)
        # method: DFS

        graph = defaultdict(list)
        for source, target in tickets:
            # if source not in graph:
            #     graph[source] = []
            graph[source].append(target)
        
        next_neighbor = {}
        for city in graph:
            graph[city].sort()
            next_neighbor[city] = 0
        
        result = []
        current = []
        
        def dfs(node: str, count_used_tickets: int) -> None:
            if count_used_tickets == len(tickets):
                result.extend(current)
                return

            for i in range(next_neighbor[node], len(graph[node])):
                neighbor = graph[node][i]
                next_neighbor[node] += 1
                current.append(neighbor)
                dfs(neighbor, count_used_tickets + 1)
                current.pop()
                next_neighbor[node] -= 1

        dfs("JFK", 0)
        result = ["JFK"] + result
        return result