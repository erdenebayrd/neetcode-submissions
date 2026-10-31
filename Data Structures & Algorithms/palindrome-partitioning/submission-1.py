class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        n = len(s)
        parts = []
        current = []

        def is_palindrome(left: int, right: int) -> bool:
            while left < right and s[left] == s[right]:
                left += 1
                right -= 1
            return left >= right

        def backtrack(left: int) -> None:
            if left >= n:
                parts.append(current[:])
                return
            
            for right in range(left, n):
                if is_palindrome(left, right):
                    current.append(s[left: right + 1])
                    backtrack(right + 1)
                    current.pop()
        
        backtrack(0)
        return parts