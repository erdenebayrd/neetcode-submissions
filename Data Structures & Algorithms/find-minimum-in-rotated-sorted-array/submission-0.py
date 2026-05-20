class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return min(nums)
        if nums[0] < nums[-1]:
            return nums[0]
        low, high = 0, len(nums)
        while low + 1 < high:
            mid = (low + high) // 2
            if nums[0] < nums[mid]:
                low = mid
            else: # nums[0] > nums[mid]
                high = mid
        return nums[high]