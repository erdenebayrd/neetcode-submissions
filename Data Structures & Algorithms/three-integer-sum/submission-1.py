class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        n = len(nums)
        for i in range(n - 2):
            if i > 0 and nums[i - 1] == nums[i]:
                continue
            left, right = i + 1, n - 1
            while left < right:
                if nums[left] + nums[right] == -nums[i]:
                    result.append([nums[i], nums[left], nums[right]])
                    left += 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                elif nums[left] + nums[right] < -nums[i]:
                    left += 1
                elif nums[left] + nums[right] > -nums[i]:
                    right -= 1
        return result