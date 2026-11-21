class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # # time: O(n)
        # # space: O(1)
        # # method: xor
        # result = 0
        n = len(nums)
        # for i in range(n):
        #     result ^= nums[i] ^ i
        # return result ^ n
        # for i in range(n + 1):
        #     curr += i
        # return curr - sum(nums)
        return n * (n + 1) // 2 - sum(nums)