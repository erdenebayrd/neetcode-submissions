from collections import defaultdict

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # # time: O(n * sum(nums))
        # # space: O(n * sum(nums))
        # # DP top down

        total = 0
        for number in nums:
            total += abs(number)
        
        if not (-total <= target <= total):
            return 0
        
        n = len(nums)

        # @cache
        # def solve(index: int, target: int) -> int:
        #     if index >= n:
        #         if target == 0:
        #             return 1
        #         return 0

        #     return solve(index + 1, target - nums[index]) + solve(index + 1, target + nums[index])
        
        # return solve(0, target)


        # # time: O(n * sum(nums))
        # # space: O(n * sum(nums))
        # # DP bottom up

        """
            dp[i][cur_target] = dp[i - 1][cur_target - nums[i]] + dp[i - 1][cur_target + nums[i]]



            -target, -target + 1 ....... 0 1 2 3 4 5 ...... target
          0 [x] [x] [x] [x] [x] [x] [x] [x] [x] [x] [x] [x] [x] [x]
          1 [x] [x] [x] [x] [x] [?] ..............................
          2                      ^
          3
          .
          .
          .
          n - 1

        """
        # time: O(n * target)
        # space: O(target)
        # method: DP bottom up

        prev = defaultdict(int)
        prev[0] = 1
        for i in range(n):
            curr = defaultdict(int)
            for cur_target in range(-abs(target), abs(target) + 1):
                curr[cur_target] = prev[cur_target - nums[i]] + prev[cur_target + nums[i]]
            prev = curr
        
        return prev[target]
