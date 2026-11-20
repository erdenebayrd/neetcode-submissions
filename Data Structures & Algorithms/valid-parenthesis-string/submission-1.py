from functools import cache

class Solution:
    def checkValidString(self, s: str) -> bool:
        # time: O(n ^ 2)
        # space: O(n ^ 2)
        # method: DP top down
        n = len(s)

        # @cache
        # def is_valid(index: int, count: int) -> bool:
        #     if count < 0:
        #         return False
        #     if index >= n:
        #         return count == 0
            
        #     if s[index] == '(':
        #         return is_valid(index + 1, count + 1)
        #     elif s[index] == ')':
        #         return is_valid(index + 1, count - 1)
        #     # asterisck
            
        #     # empty
        #     result = is_valid(index + 1, count)

        #     # open
        #     result |= is_valid(index + 1, count + 1)

        #     # closing
        #     result |= is_valid(index + 1, count - 1)
        #     return result
        
        # return is_valid(0, 0)

        """
                        0 1 2 3 4    <------ 
            (        0    T
            (        1      T
            *        2    T T T
            *        3  T T T T T
            )        4  T T T T F
        """
        if n <= 0:
            return True
        if s[0] == ')':
            return False
        
        
        dp = [[False] * (n + 1) for _ in range(n)]

        if s[0] == '*':
            dp[0][0] = True
        dp[0][1] = True
        for i in range(1, n):
            for count_open in range(n + 1):
                if s[i] == '(':
                    if count_open - 1 >= 0:
                        dp[i][count_open] = dp[i - 1][count_open - 1]
                elif s[i] == ')':
                    if count_open + 1 < n:
                        dp[i][count_open] = dp[i - 1][count_open + 1]
                else: # *
                    # empty case
                    dp[i][count_open] = dp[i - 1][count_open]

                    # open case
                    if count_open - 1 >= 0:
                        dp[i][count_open] |= dp[i - 1][count_open - 1]
                    
                    # close case
                    if count_open + 1 < n:
                        dp[i][count_open] |= dp[i - 1][count_open + 1]
        
        return dp[n - 1][0]







