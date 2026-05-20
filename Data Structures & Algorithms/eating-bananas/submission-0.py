import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def can(speed: int) -> bool:
            total = 0
            for pile in piles:
                total += math.ceil(pile / speed)
            return total <= h

        n = len(piles)
        low, high = 0, max(piles) + 1
        while low + 1 < high:
            mid_speed = (low + high) // 2
            if can(mid_speed):
                high = mid_speed
            else:
                low = mid_speed
        return high