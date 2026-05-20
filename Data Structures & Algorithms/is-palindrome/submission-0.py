class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        def is_valid(ch: str) -> bool:
            return 'a' <= ch <= 'z' or '0' <= ch <= '9'

        n = len(s)
        left, right = 0, n - 1
        while left < right:
            if not is_valid(s[left]):
                left += 1
            elif not is_valid(s[right]):
                right -= 1
            else:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
        return True