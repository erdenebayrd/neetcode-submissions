class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        n = len(s)
        left = 0
        length = 0
        for right in range(n):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
            seen.add(s[right])
            length = max(length, right - left + 1)
        return length