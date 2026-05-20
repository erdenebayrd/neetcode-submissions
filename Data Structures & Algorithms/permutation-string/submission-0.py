from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        count = Counter(s1)
        current = Counter()
        count_equal = 0

        def add(ch: str) -> None:
            nonlocal count_equal
            if ch not in count:
                return
            current[ch] += 1
            if current[ch] == count[ch]:
                count_equal += 1
        
        def remove(ch: str) -> None:
            nonlocal count_equal
            if ch not in count:
                return
            current[ch] -= 1
            if current[ch] + 1 == count[ch]:
                count_equal -= 1
        
        for i in range(len(s1) - 1):
            add(s2[i])
        
        for i in range(len(s1) - 1, len(s2)):
            add(s2[i])
            if count_equal == len(count):
                return True
            remove(s2[i - len(s1) + 1])
        return False