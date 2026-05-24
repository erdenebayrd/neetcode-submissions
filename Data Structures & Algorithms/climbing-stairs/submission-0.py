class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        
        prev_prev, prev = 1, 2
        current = 0
        for i in range(3, n + 1):
            current = prev_prev + prev
            prev_prev = prev
            prev = current
        return current