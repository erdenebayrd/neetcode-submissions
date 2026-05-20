from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counter = defaultdict(int)
        for ch in s:
            counter[ch] += 1
        for ch in t:
            counter[ch] -= 1
        for ch in counter:
            if counter[ch] != 0:
                return False
        return True