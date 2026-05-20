class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        occurrences = {}
        for i in range(len(nums)):
            need = target - nums[i]
            if need in occurrences:
                return [occurrences[need], i]
            occurrences[nums[i]] = i
        return []