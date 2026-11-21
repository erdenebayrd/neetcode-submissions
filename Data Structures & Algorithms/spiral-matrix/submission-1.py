class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # time: O(rows * cols)
        # space: O(1) excluding output array
        # method: Simulation
        
        rows = len(matrix)
        cols = len(matrix[0])

        top = 0
        bottom = rows - 1
        left = 0
        right = cols - 1

        result = []
        while top <= bottom and left <= right:
            # go right
            for col in range(left, right + 1):
                result.append(matrix[top][col])
            top += 1
            if top > bottom: break

            # go bottom
            for row in range(top, bottom + 1):
                result.append(matrix[row][right])
            right -= 1
            if left > right: break

            # go left
            for col in range(right, left - 1, -1):
                result.append(matrix[bottom][col])
            bottom -= 1
            if top > bottom: break

            # go up
            for row in range(bottom, top - 1, -1):
                result.append(matrix[row][left])
            left += 1
            if left > right: break
            
        return result