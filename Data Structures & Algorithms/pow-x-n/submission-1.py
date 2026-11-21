class Solution:
    def myPow(self, x: float, n: int) -> float:
        # time: O(log n)
        # space: O(1)
        # method: 

        def my_pow(x: float, n: int) -> float:
            result = 1.0
            while n:
                if n & 1: # n is odd
                    n -= 1
                    result = result * x
                else:
                    n //= 2
                    x = x * x
            return result
        
        x = my_pow(x, abs(n))
        if n < 0: # negative
            x = 1.0 / x
        return x