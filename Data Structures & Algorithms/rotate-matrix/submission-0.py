class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # time: O(n ^ 2)
        # space: O(1)
        # method: simulation

        def next_coordinate(row: int, col: int, length: int) -> list:
            next_col = length - 1 - row
            next_row = col
            return [next_row, next_col]

        def get_coordinates(row: int, col: int, length) -> list: # returns 4 coordinates starting from row & col
            result = []
            for _ in range(4):
                result.append(row)
                result.append(col)
                row, col = next_coordinate(row, col, length)
            return result
                
        
        n = len(matrix)
        length = n
        for i in range(n // 2):
            for j in range(i, i + length - 1):
                p1_row, p1_col, p2_row, p2_col, p3_row, p3_col, p4_row, p4_col = get_coordinates(i, j, length)
                matrix[p1_row][p1_col], matrix[p2_row][p2_col], matrix[p3_row][p3_col], matrix[p4_row][p4_col] = matrix[p4_row][p4_col], matrix[p1_row][p1_col], matrix[p2_row][p2_col], matrix[p3_row][p3_col]
            length -= 2