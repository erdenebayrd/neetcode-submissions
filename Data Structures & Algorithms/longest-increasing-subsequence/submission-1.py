import bisect

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # time: O(N log N) N is len of nums
        # space: O(N)
        # method: DP + bin search
        n = len(nums)
        arr = []
        for number in nums:
            index = bisect.bisect_left(arr, number)
            if index == len(arr):
                arr.append(number)
            else:
                arr[index] = number
            
        return len(arr)