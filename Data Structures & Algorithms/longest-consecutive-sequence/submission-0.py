from functools import cache
from collections import defaultdict

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n = len(nums)
        existed = defaultdict(bool)
        for num in nums:
            existed[num] = True
        
        @cache
        def longestConsecutiveFrom(startingValue: int) -> int: # amorized O(N), means total O(N) for all calls
            if existed[startingValue] is False:
                return 0
            return 1 + longestConsecutiveFrom(startingValue + 1)
        
        result = 0
        for num in nums:
            result = max(result, longestConsecutiveFrom(num))
        return result