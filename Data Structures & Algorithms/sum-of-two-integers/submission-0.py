class Solution:
    def getSum(self, a: int, b: int) -> int:
        # O(log n) 
        # space: O(1)
        # method: bit
        result = 0
        carry = 0
        n = max(a.bit_length(), b.bit_length())
        for i in range(n):
            a_bit = (a >> i) & 1
            b_bit = (b >> i) & 1
            if a_bit == 0 and b_bit == 0:
                result |= (carry << i)
                carry = 0
            elif (a_bit ^ b_bit) == 1:
                if carry == 0:
                    result |= (1 << i)
            else: # both 1
                if carry == 0:
                    carry = 1
                else:
                    result |= (1 << i)
        
        result |= (carry << n)    
        
        return result