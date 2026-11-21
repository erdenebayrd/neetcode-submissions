class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # time: O(n)
        # space: O(1)
        # method: xor
        value = 0
        for number in nums:
            value ^= number
        return value