class Solution:
    def longestPalindrome(self, s: str) -> str:
        # # time: O(N ^ 2) N is len of s
        # # space: O(1)
        # # method: expand around center
        # n = len(s)

        # def helper(left: int, right: int) -> tuple: # O(N)
        #     while left - 1 >= 0 and right + 1 < n and s[left - 1] == s[right + 1]:
        #         left -= 1
        #         right += 1
        #     return (left, right)
        
        # result = [0, 0]
        # for i in range(n):
        #     # odd length
        #     left, right = helper(i, i)
        #     if result[1] - result[0] < right - left:
        #         result = [left, right]
            
        #     # even length
        #     left, right = helper(i + 1, i)
        #     if result[1] - result[0] < right - left:
        #         result = [left, right]
        
        # return s[result[0]: result[1] + 1]

        # manacher algo
        # time: O(N)
        # space: O(N)
        # method: manacher
        text = "#" + "#".join(list(s)) + "#"
        n = len(text)
        length = [0] * n
        left = right = -1
        for i in range(n):
            if i <= right:
                mirror_index = left + right - i
                length[i] = min(length[mirror_index], right - i)
            
            while i - length[i] - 1 >= 0 and i + length[i] + 1 < n and text[i - length[i] - 1] == text[i + length[i] + 1]:
                length[i] += 1
            
            if i + length[i] > right:
                left, right = i - length[i], i + length[i]
        
        max_length = max(length)
        start_index = -1
        for i in range(n):
            if max_length == length[i]:
                original_index = i // 2
                start_index = original_index - max_length // 2
                break
        
        return s[start_index: start_index + max_length]
