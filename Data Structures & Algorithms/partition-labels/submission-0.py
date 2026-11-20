class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # time: O(n) n is len of s
        # space: O(n)
        # method: sliding window

        n = len(s)
        pos = {}
        for i in range(n):
            pos[s[i]] = i # updating pos
        
        left = 0
        index = 0
        arr = []
        while index < n:
            right = pos[s[index]]
            while index < n and index <= right:
                right = max(right, pos[s[index]])
                index += 1

            right = index
            arr.append(right - left)
            left = right
        
        return arr