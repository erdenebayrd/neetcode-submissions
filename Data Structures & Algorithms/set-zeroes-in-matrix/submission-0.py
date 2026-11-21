class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        # time: O(rows * cols)
        # space: O(1)
        # method: simulation
        rows = len(matrix)
        cols = len(matrix[0])

        inf = float('inf')
        for row in range(rows):
            for col in range(cols):
                if matrix[row][col] == 0:
                    break
            else:
                continue
            
            for col in range(cols):
                if matrix[row][col] == 0:
                    continue
                matrix[row][col] = inf
        
        for col in range(cols):
            for row in range(rows):
                if matrix[row][col] == 0:
                    break
            else:
                continue
            
            for row in range(rows):
                if matrix[row][col] == 0:
                    continue
                matrix[row][col] = inf
        
        for row in range(rows):
            for col in range(cols):
                if matrix[row][col] == inf:
                    matrix[row][col] = 0