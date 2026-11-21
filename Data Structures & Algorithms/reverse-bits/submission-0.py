class Solution:
    def reverseBits(self, n: int) -> int:
        # time: O(1)
        # space: O(1)
        # method: bit

        result = 0
        for i in range(32):
            if (1 << i) & n:
                result |= (1 << (31 - i))
        return result