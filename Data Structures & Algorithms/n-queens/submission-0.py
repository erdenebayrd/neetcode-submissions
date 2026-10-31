class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        boards = []
        current = []

        def can(state: int, current: list) -> bool:
            for i in range(len(current) - 1, -1, -1):
                if state & current[i]: # same col
                    return False
                
                shift = len(current) - i
                
                if (state << shift) & current[i]: # same diagonal 1
                    return False
                
                if (state >> shift) & current[i]: # same diagonal 2
                    return False
            
            return True


        def backtrack(row: int) -> None:
            if row >= n:
                boards.append(current[:])
                return
            
            for col in range(n):
                state = 1 << col
                if can(state, current):
                    current.append(state)
                    backtrack(row + 1)
                    current.pop()

        def convert(row: int) -> str:
            result = []
            for i in range(n):
                if (1 << i) & row:
                    result.append("Q")
                else:
                    result.append(".")
            return "".join(result)

        backtrack(0)

        result = []
        for board in boards:
            current = []
            for row in board:
                current.append(convert(row))
            result.append(current[:])
        return result
