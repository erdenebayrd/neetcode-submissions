import heapq
from collections import deque, Counter

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)

        tasks = [-count[task] for task in count]
        heapq.heapify(tasks)
        queue = deque()

        current_time = 0
        while queue or tasks:
            while queue and queue[0][1] <= current_time:
                freq, _ = queue.popleft()
                heapq.heappush(tasks, freq)

            if tasks:
                freq = heapq.heappop(tasks)
                freq += 1
                current_time += 1
                if freq != 0:
                    queue.append((freq, current_time + n)) # the time that task can come back to CPU
            else: # idle time
                current_time = queue[0][1]
        return current_time