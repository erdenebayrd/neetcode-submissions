class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # time: O(N)
        # space: O(1)
        # method: 

        def solve(left: int, right: int) -> float:
            if left > right:
                return float('-inf')
            first = last = -1
            count = 0
            for i in range(left, right + 1):
                if nums[i] < 0:
                    count += 1
                    if first == -1:
                        first = i
                    last = i
            
            if count % 2 == 0: # even
                result = 1
                for i in range(left, right + 1):
                    result *= nums[i]
                return result
            
            # odd
            # left -> last - 1
            # first + 1, right
            return max(solve(left, last - 1), solve(first + 1, right))


        n = len(nums)
        result = float('-inf')
        for i in range(n):
            if nums[i] == 0:
                result = 0
        
        left = 0
        for right in range(n):
            if nums[right] == 0:
                result = max(result, solve(left, right - 1))
                left = right + 1
        
        result = max(result, solve(left, n - 1))

        return result




