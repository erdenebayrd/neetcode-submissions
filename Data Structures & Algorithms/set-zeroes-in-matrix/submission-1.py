class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        # time: O(rows * cols)
        # space: O(1)
        # method: simulation
        rows = len(matrix)
        cols = len(matrix[0])

        first_row = False
        first_col = False
        for col in range(cols):
            if matrix[0][col] == 0:
                first_row = True
                break
        
        for row in range(rows):
            if matrix[row][0] == 0:
                first_col = True
                break
        
        for row in range(1, rows):
            for col in range(1, cols):
                if matrix[row][col] == 0:
                    matrix[0][col] = 0 # marking this entire column need to become 0
        
        for col in range(1, cols):
            for row in range(1, rows):
                if matrix[row][col] == 0:
                    matrix[row][0] = 0 # marking this entire row need to become 0
        
        for row in range(1, rows):
            for col in range(1, cols):
                if matrix[row][0] == 0 or matrix[0][col] == 0:
                    matrix[row][col] = 0
        
        if first_row:
            for col in range(cols):
                matrix[0][col] = 0
        
        if first_col:
            for row in range(rows):
                matrix[row][0] = 0