from functools import cache

class Solution:
    def checkValidString(self, s: str) -> bool:
        # time: O(n ^ 2)
        # space: O(n ^ 2)
        # method: DP top down
        n = len(s)

        @cache
        def is_valid(index: int, count: int) -> bool:
            if count < 0:
                return False
            if index >= n:
                return count == 0
            
            if s[index] == '(':
                return is_valid(index + 1, count + 1)
            elif s[index] == ')':
                return is_valid(index + 1, count - 1)
            # asterisck
            
            # empty
            result = is_valid(index + 1, count)

            # open
            result |= is_valid(index + 1, count + 1)

            # closing
            result |= is_valid(index + 1, count - 1)
            return result
        
        return is_valid(0, 0)
