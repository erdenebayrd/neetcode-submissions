class Solution:
    def isHappy(self, n: int) -> bool:
        
        def next_number(number: int) -> int:
            result = 0
            while number:
                digit = number % 10
                result += digit * digit
                number //= 10
            return result
        
        hare = next_number(next_number(n))
        tortoise = next_number(n)
        while hare != tortoise:
            hare = next_number(next_number(hare))
            tortoise = next_number(tortoise)

        return hare == 1