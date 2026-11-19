class Solution:
    def longestPalindrome(self, s: str) -> str:
        # time: O(N ^ 2) N is len of s
        # space: O(1)
        # method: brute force
        n = len(s)

        def helper(left: int, right: int) -> tuple: # O(N)
            while left - 1 >= 0 and right + 1 < n and s[left - 1] == s[right + 1]:
                left -= 1
                right += 1
            return (left, right)
        
        result = []
        for i in range(n):
            # odd length
            left, right = helper(i, i)
            if not result or result[1] - result[0] < right - left:
                result = [left, right]
            
            # even length
            left, right = helper(i + 1, i)
            if result[1] - result[0] < right - left:
                result = [left, right]
        
        return s[result[0]: result[1] + 1]