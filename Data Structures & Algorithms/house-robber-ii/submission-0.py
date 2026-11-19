class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1:
            return sum(nums)

        def helper(left: int, right: int) -> int:
            take = not_take = 0
            for i in range(left, right + 1):
                take, not_take = nums[i] + not_take, max(take, not_take)
            return max(take, not_take)
        
        return max(helper(0, n - 2), helper(1, n - 1))