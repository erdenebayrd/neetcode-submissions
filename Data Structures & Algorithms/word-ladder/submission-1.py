from collections import deque

class Solution:
    def ladderLength(self, begin_word: str, end_word: str, word_list: List[str]) -> int:
        # V = len(word_list) vertices, E = len(word_list) ^ 2, M is length of begin_word
        # time: O(V + E * M)
        # space: O(V)
        # method: BFS
        inf = float('inf')
        n = len(word_list) + 1
        graph = [[] for _ in range(n)] # 0 as begin_word
        if end_word not in word_list:
            return 0
        
        target = word_list.index(end_word) + 1
        
        def count(word_u: str, word_v: str) -> int:
            diff = 0
            for i in range(len(word_u)):
                if word_u[i] != word_v[i]:
                    diff += 1
            return diff

        for i in range(len(word_list)):
            if count(begin_word, word_list[i]) == 1:
                graph[0].append(i + 1)
                graph[i + 1].append(0)

            for j in range(i + 1, len(word_list)):
                if count(word_list[i], word_list[j]) == 1:
                    graph[i + 1].append(j + 1)
                    graph[j + 1].append(i + 1)
        
        queue = deque()
        queue.append(0) # begin_word index
        dist = [inf] * n
        dist[0] = 1

        while queue:
            node = queue.popleft()
            for neighbor in graph[node]:
                if dist[neighbor] > dist[node] + 1:
                    dist[neighbor] = dist[node] + 1
                    queue.append(neighbor)
        
        cost = dist[target]
        if cost == inf:
            cost = 0

        return cost