class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # time: O(n)
        # space: O(n) for output array
        # method: simulation

        n = len(digits)
        saved_number = 1
        result = digits[:]
        for i in range(n - 1, -1, -1):
            number = saved_number + result[i]
            result[i] = number % 10
            saved_number = number // 10
        
        if saved_number:
            result.insert(0, saved_number)

        return result