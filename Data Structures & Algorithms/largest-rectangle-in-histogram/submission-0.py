class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        next_lower = [n] * n
        stack = []
        for i in range(n - 1, -1, -1):
            while stack and heights[i] <= heights[stack[-1]]:
                stack.pop()
            if stack:
                next_lower[i] = stack[-1]
            stack.append(i)
        
        prev_lower = [-1] * n
        stack = []
        for i in range(n):
            while stack and heights[i] <= heights[stack[-1]]:
                stack.pop()
            if stack:
                prev_lower[i] = stack[-1]
            stack.append(i)
        
        result = 0
        for i in range(n):
            height = heights[i]
            left = prev_lower[i] + 1
            right = next_lower[i] - 1
            width = right - left + 1
            result = max(result, height * width)
        return result
