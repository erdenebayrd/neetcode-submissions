import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = []
        for x, y in points:
            dist = x * x + y * y
            heapq.heappush(distances, (dist, x, y))
        
        result = []
        while k:
            _, x, y = heapq.heappop(distances)
            result.append([x, y])
            k -= 1
        return result