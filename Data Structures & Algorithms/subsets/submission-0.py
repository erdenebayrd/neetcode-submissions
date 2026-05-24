class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        result = []
        for bitmask in range(1 << n):
            current = []
            for i in range(n):
                if bitmask & (1 << i):
                    current.append(nums[i])
            result.append(current)
        return result