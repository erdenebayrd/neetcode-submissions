class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # time: O(rows * cols)
        # space: O(1) excluding output array
        # method: Simulation
        
        rows = len(matrix)
        cols = len(matrix[0])

        #              right            down             left             up
        directions = [[0, 1, cols, 1], [1, 0, rows, -1], [0, -1, -1, -1], [-1, 0, -1, 1]]
        
        result = []
        row = col = current_dir = 0

        for _ in range(rows * cols):
            result.append(matrix[row][col])

            delta_row, delta_col, limit, delta = directions[current_dir]
            next_row, next_col = row + delta_row, col + delta_col
            if (current_dir % 2 ==0 and next_col == limit) or (current_dir % 2 == 1 and next_row == limit):
                directions[(current_dir - 1) % len(directions)][2] += delta
                current_dir = (current_dir + 1) % len(directions)
                delta_row, delta_col, limit, delta = directions[current_dir]
                next_row, next_col = row + delta_row, col + delta_col
            row, col = next_row, next_col
        return result