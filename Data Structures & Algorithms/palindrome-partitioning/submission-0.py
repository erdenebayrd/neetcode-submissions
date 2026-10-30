class Solution:
    def partition(self, s: str) -> List[List[str]]:
        # time: O(n * 2 ^ n)
        # space: O(n * 2 ^ n)
        # method: bitmask, brute force

        def is_palindrome(left: int, right: int) -> bool: # O(n)
            while left < right and s[left] == s[right]:
                left += 1
                right -= 1
            return left >= right

        n = len(s)
        parts = []
        seen = set()
        for bitmask in range(1 << n):
            left = 0
            subset = []
            flag = True
            if bitmask in seen:
                continue
            seen.add(bitmask ^ ((1 << n) - 1)) # reversed bits

            for right in range(n):
                if (bitmask >> left) & 1 != (bitmask >> right) & 1:
                    if not is_palindrome(left, right - 1):
                        flag = False
                        break
                    subset.append(s[left:right])
                    left = right

            flag &= is_palindrome(left, right)
            subset.append(s[left:right + 1])
            if flag:
                parts.append(subset[:])
        
        return parts