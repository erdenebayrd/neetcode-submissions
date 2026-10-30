class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # time: O(rows * cols * 4 ^ len(word))
        # space: O(len(word))
        # method: backtrack, brute force
        seen = set()
        n = len(word)
        rows = len(board)
        cols = len(board[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def backtrack(row: int, col: int, index: int) -> bool:
            if index >= n:
                return True
            
            if word[index] != board[row][col]:
                return False

            seen.add((row, col))
            for delta_row, delta_col in directions:
                next_row, next_col = delta_row + row, delta_col + col
                if next_row < 0 or next_row >= rows or next_col < 0 or next_col >= cols or (next_row, next_col) in seen:
                    continue
                
                if backtrack(next_row, next_col, index + 1):
                    return True
            seen.remove((row, col))
            return False
        
        for row in range(rows):
            for col in range(cols):
                if backtrack(row, col, 0):
                    return True
        return False