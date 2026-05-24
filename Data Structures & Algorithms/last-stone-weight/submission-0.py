import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-stone for stone in stones]
        heapq.heapify(stones)
        while len(stones) >= 2:
            largest_stone = -heapq.heappop(stones)
            second_largest_stone = -heapq.heappop(stones)
            remain = largest_stone - second_largest_stone
            if remain > 0:
                heapq.heappush(stones, -remain)
        if stones:
            return -stones[0]
        return 0