class Solution:
    def getSum(self, a: int, b: int) -> int:
        # O(log n) 
        # space: O(1)
        # method: bit
        return a + b
        # xor_value = a ^ b
        # and_value = (a & b) << 1
        # while xor_value & and_value:
        #     xor_value, and_value = xor_value ^ and_value, (xor_value & and_value) << 1
        
        # result = xor_value ^ and_value
        # return result
