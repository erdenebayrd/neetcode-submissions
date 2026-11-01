from collections import deque

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        # time: O(rows * cols)
        # space: O(rows * cols)
        # method: multisouce BFS
        rows = len(board)
        cols = len(board[0])

        if rows == 1 or cols == 1:
            return

        seen = set()
        queue = deque()
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        for row in range(rows):
            if board[row][0] == 'O':
                seen.add((row, 0))
                queue.append((row, 0))

            if board[row][cols - 1] == 'O':
                seen.add((row, cols - 1))
                queue.append((row, cols - 1))
        
        for col in range(cols):
            if board[0][col] == 'O':
                seen.add((0, col))
                queue.append((0, col))
            
            if board[rows - 1][col] == 'O':
                seen.add((rows - 1, col))
                queue.append((rows - 1, col))
        
        while queue:
            row, col = queue.popleft()
            for delta_row, delta_col in directions:
                next_row, next_col = row + delta_row, col + delta_col
                if next_row < 0 or next_row >= rows or next_col < 0 or next_col >= cols or (next_row, next_col) in seen or board[next_row][next_col] != 'O':
                    continue
                seen.add((next_row, next_col))
                queue.append((next_row, next_col))
        
        for row in range(rows):
            for col in range(cols):
                if board[row][col] == 'O' and (row, col) not in seen:
                    board[row][col] = 'X'
