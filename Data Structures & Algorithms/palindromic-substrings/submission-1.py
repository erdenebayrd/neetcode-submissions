class Solution:
    def countSubstrings(self, s: str) -> int:
        # time: O(N ^ 2)
        # space: O(1)
        # method: expand around center

        n = len(s)

        def helper(left: int, right: int) -> tuple: # O(N)
            while left - 1 >= 0 and right + 1 < n and s[left - 1] == s[right + 1]:
                left -= 1
                right += 1
            return (left, right)
        
        count = 0
        for i in range(n):
            # odd length
            left, right = helper(i, i)
            length = right - left + 1
            count += (length + 1) // 2

            # even length
            left, right = helper(i + 1, i)
            length = right - left + 1
            count += (length + 1) // 2

        return count