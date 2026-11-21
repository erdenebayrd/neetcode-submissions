class Solution:
    def isHappy(self, n: int) -> bool:
        
        def next_number(number: int) -> int:
            result = 0
            while number:
                digit = number % 10
                result += digit * digit
                number //= 10
            return result
        
        seen = set()
        while n != 1 and n not in seen:
            seen.add(n)
            n = next_number(n)
        
        return n == 1