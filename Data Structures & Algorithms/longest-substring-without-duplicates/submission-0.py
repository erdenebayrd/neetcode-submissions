class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        n = len(s)
        left = 0
        result = 0
        for right in range(n):
            seen.add(s[right])
            while len(seen) < right - left + 1:
                while s[left] != s[right]:
                    seen.remove(s[left])
                    left += 1
                left += 1
            result = max(result, right - left + 1)
        return result