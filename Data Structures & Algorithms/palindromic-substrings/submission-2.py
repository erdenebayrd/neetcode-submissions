class Solution:
    def countSubstrings(self, s: str) -> int:
        # # time: O(N ^ 2)
        # # space: O(1)
        # # method: expand around center

        # n = len(s)

        # def helper(left: int, right: int) -> tuple: # O(N)
        #     while left - 1 >= 0 and right + 1 < n and s[left - 1] == s[right + 1]:
        #         left -= 1
        #         right += 1
        #     return (left, right)
        
        # count = 0
        # for i in range(n):
        #     # odd length
        #     left, right = helper(i, i)
        #     length = right - left + 1
        #     count += (length + 1) // 2

        #     # even length
        #     left, right = helper(i + 1, i)
        #     length = right - left + 1
        #     count += (length + 1) // 2

        # return count

        # time: O(N)
        # space: O(N)
        # method: manacher algo

        text = "#" + "#".join(s) + "#"
        n = len(text)
        left = right = -1
        length = [0] * n

        for i in range(n):
            if i <= right:
                mirror_index = right - i + left
                length[i] = min(length[mirror_index], right - i)
            
            while i - length[i] - 1 >= 0 and i + length[i] + 1 < n and text[i - length[i] - 1] == text[i + length[i] + 1]:
                length[i] += 1
            
            if i + length[i] > right:
                left, right = i - length[i], i + length[i]
        
        count = 0
        for current_length in length:
            count += (current_length + 1) // 2
        return count