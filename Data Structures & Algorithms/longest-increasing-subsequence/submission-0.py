class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # time: O(N log N) N is len of nums
        # space: O(N)
        # method: DP + bin search
        inf = float('inf')
        n = len(nums)
        arr = [nums[0]]
        for i in range(1, n):
            if arr[-1] < nums[i]:
                arr.append(nums[i])
            else: # arr[-1] >= nums[i]
                low, high = -1, len(arr)
                while low + 1 < high:
                    mid = (low + high) // 2
                    if arr[mid] < nums[i]:
                        low = mid
                    else:
                        high = mid
                arr[high] = nums[i]
        return len(arr)