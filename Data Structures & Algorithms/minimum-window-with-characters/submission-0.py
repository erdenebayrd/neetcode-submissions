from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        count = Counter(t)
        count_pattern = Counter()
        left = 0
        count_equal = 0
        longest = float('inf')
        indices = [-1, -1]
        n = len(s)
        for right in range(n):
            if s[right] not in count:
                continue
            count_pattern[s[right]] += 1
            if count_pattern[s[right]] == count[s[right]]:
                count_equal += 1
            while count_equal == len(count):
                if right - left + 1 < longest:
                    indices = [left, right]
                    longest = right - left + 1
                if s[left] in count:
                    count_pattern[s[left]] -= 1
                    if count_pattern[s[left]] + 1 == count[s[left]]:
                        count_equal -= 1
                left += 1
        if indices[0] == -1:
            return ""
        left, right = indices
        return s[left: right + 1]