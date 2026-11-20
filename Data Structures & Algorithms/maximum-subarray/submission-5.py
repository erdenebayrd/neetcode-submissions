class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # # time: O(n)
        # # space: O(1)
        # # method: cumulative sum
        # n = len(nums)
        
        # current_min = 0
        # current_sum = 0
        
        # result = float('-inf')
        # for i in range(n):
        #     current_sum += nums[i]
        #     result = max(result, current_sum - current_min)
        #     current_min = min(current_min, current_sum)

        # return result

        # time: O(n)
        # space: O(1)
        # method: Kadane

        best_sum = float('-inf')
        current_sum = float('-inf')

        for number in nums:
            current_sum = max(number, current_sum + number) # until this point, best possible sum till this one (must include this one)
            best_sum = max(best_sum, current_sum)
        
        return best_sum