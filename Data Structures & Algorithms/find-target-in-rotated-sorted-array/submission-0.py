class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def find_min_index(nums: List[int]) -> int:
            if len(nums) <= 2:
                if min(nums) == nums[0]:
                    return 0
                return 1
            if nums[0] < nums[-1]:
                return 0
            
            low, high = 0, len(nums)
            while low + 1 < high:
                mid = (low + high) // 2
                if nums[0] < nums[mid]:
                    low = mid
                else:
                    high = mid
            return high
        
        def binary_search(left: int, right: int, target: int) -> -1:
            low, high = left - 1, right + 1
            while low + 1 < high:
                mid = (low + high) // 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] < target:
                    low = mid
                else:
                    high = mid
            return -1
        
        min_index = find_min_index(nums)
        if min_index == 0: # no rotation
            return binary_search(0, len(nums) - 1, target)

        return max(binary_search(0, min_index - 1, target), binary_search(min_index, len(nums) - 1, target))