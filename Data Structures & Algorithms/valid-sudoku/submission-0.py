class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # time: O(N ^ 2)
        # space: O(N)

        def isRowValid(row: int) -> bool: # O(N)
            seen = set()
            for column in range(len(board[row])):
                cell = board[row][column]
                if cell == ".":
                    continue
                if cell in seen:
                    return False
                seen.add(cell)
            return True
        
        def isColumnValid(column: int) -> bool: # O(N)
            seen = set()
            for row in range(len(board)):
                cell = board[row][column]
                if cell == ".":
                    continue
                if cell in seen:
                    return False
                seen.add(cell)
            return True
        
        def isTripleSquareValid(topLeftRow: int, topLeftColumn: int) -> bool: # O(9)
            seen = set()
            for row in range(topLeftRow, topLeftRow + 3):
                for column in range(topLeftColumn, topLeftColumn + 3):
                    cell = board[row][column]
                    if cell == ".":
                        continue
                    if cell in seen:
                        return False
                    seen.add(cell)
            return True
        
        for row in range(len(board)):
            if isRowValid(row) is False:
                return False
        
        for column in range(len(board[0])):
            if isColumnValid(column) is False:
                return False
        
        for row in range(0, len(board), 3):
            for column in range(0, len(board[row]), 3):
                if isTripleSquareValid(row, column) is False:
                    return False
        
        return True