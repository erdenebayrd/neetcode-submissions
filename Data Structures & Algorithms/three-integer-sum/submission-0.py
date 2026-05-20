class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        n = len(nums)
        last_added_min = float('inf')
        last_added_max = float('-inf')
        for i in range(n - 2):
            left, right = i + 1, n - 1
            while left < right:
                if nums[left] + nums[right] == -nums[i]:
                    if last_added_min == nums[i] and last_added_max == nums[right]:
                        left += 1
                    else:
                        last_added_min = nums[i]
                        last_added_max = nums[right]
                        result.append([nums[i], nums[left], nums[right]])
                elif nums[left] + nums[right] < -nums[i]:
                    left += 1
                elif nums[left] + nums[right] > -nums[i]:
                    right -= 1
        return result