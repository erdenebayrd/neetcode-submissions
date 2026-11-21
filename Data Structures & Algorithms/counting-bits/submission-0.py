class Solution:
    def countBits(self, n: int) -> List[int]:
        # time: O(n)
        # space: O(n) for ouput array
        # method: bit manipulation

        result = [0] * (n + 1)
        for i in range(1, n + 1):
            prev_number = i - 1
            diff = prev_number ^ i
            result[i] = result[i - 1] - diff.bit_length() + 2
        return result