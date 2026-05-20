class Solution:
    def isValid(self, s: str) -> bool:
        
        def flip(ch: str) -> str:
            if "]" == ch:
                return "["
            if "}" == ch:
                return "{"
            if ")" == ch:
                return "("
            assert False

        count = {"(": 0, "{": 0, "[": 0}
        for ch in s:
            if ch in count:
                count[ch] += 1
            else:
                count[flip(ch)] -= 1
                if count[flip(ch)] < 0:
                    return False
        for key in count:
            if count[key] > 0:
                return False
        return True