class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        result = []
        for bitmask in range(1 << n):
            current = []
            while bitmask:
                last_bit = bitmask & -bitmask
                current.append(nums[last_bit.bit_length() - 1])
                bitmask -= last_bit
            result.append(current)
        return result