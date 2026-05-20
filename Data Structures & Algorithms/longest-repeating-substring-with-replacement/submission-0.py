from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        n = len(s)
        count = defaultdict(int)
        current_max = 0
        result = 0
        for right in range(n):
            count[s[right]] += 1
            current_max = max(current_max, count[s[right]])
            if right - left + 1 - current_max > k:
                count[s[left]] -= 1
                left += 1
            result = max(result, right - left + 1)
        return result