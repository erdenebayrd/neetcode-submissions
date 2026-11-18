from collections import deque

class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        # time: O(V * E) V is number of chars, E is length of words array
        # space: O(V)
        # method: Kahn algo cycle detection

        n = len(words)
        graph = {}
        indegree = {}
        for word in words:
            for ch in word:
                graph[ch] = []
                indegree[ch] = 0
        
        for i in range(1, n):
            length = min(len(words[i]), len(words[i - 1]))
            for j in range(length):
                if words[i - 1][j] != words[i][j]:
                    graph[words[i - 1][j]].append(words[i][j])
                    indegree[words[i][j]] += 1
                    break
            else:
                if len(words[i - 1]) > len(words[i]):
                    return ""
        
        path = []
        queue = deque()
        for node in graph:
            if indegree[node] == 0:
                queue.append(node)
                path.append(node)

        while queue:
            node = queue.popleft()
            for neighbor in graph[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
                    path.append(neighbor)

        for node in graph:
            if indegree[node]: # cycle detected
                return "" 

        return "".join(path)