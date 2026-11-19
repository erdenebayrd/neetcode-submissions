class Solution:
    def rob(self, nums: List[int]) -> int:
        # time: O(N)
        # space: O(1)
        # method: DP
        take = not_take = 0
        for value in nums:
            take, not_take = value + not_take, max(take, not_take)
        return max(take, not_take)