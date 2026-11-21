class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        # time: O(n * m) n len of num1, m is len of num2
        # space: O(n + m)
        # method: simulation

        # one comment is there is faster method like FFT/NTT which can work O((n + m) log (n + m)), but thats too complicated I guess

        if len(num1) == 1 and num1[0] == '0':
            return "0"

        if len(num2) == 1 and num2[0] == '0':
            return "0"
        
        n, m = len(num1), len(num2)
        result = [0] * (n + m + 1)
        index = n + m
        for i in range(n - 1, -1, -1):
            index = m + 1 + i
            for j in range(m - 1, -1, -1):
                number = int(num1[i]) * int(num2[j]) + result[index]
                last_digit = number % 10
                remainder = number // 10
                result[index] = last_digit
                result[index - 1] += remainder
                index -= 1
        
        result = result[::-1]
        while result and result[-1] == 0:
            result.pop()
        result = result[::-1]
        return "".join(str(digit) for digit in result)