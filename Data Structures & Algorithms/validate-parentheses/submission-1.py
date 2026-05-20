class Solution:
    def isValid(self, s: str) -> bool:
        def flip(ch: str) -> str:
            if ")" == ch:
                return "("
            if "}" == ch:
                return "{"
            if "]" == ch:
                return "["
            assert False
            
        stack = []
        for ch in s:
            if "(" == ch or "[" == ch or "{" == ch:
                stack.append(ch)
            else:
                if not stack or stack[-1] != flip(ch):
                    return False
                stack.pop()
        return not stack