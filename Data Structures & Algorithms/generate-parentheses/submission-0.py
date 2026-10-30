class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # time: O(n * 2 ^ n)
        # space: O(n * 2 ^ n)
        # backtrack

        parentheses = []
        current = []
        def backtrack(current_open: int, current_have: int) -> None:
            if current_open == current_have == 0:
                parentheses.append("".join(current))
                return
            
            if current_have: # open
                current.append("(")
                backtrack(current_open + 1, current_have - 1)
                current.pop()
            
            if current_open: # close
                current.append(")")
                backtrack(current_open - 1, current_have)
                current.pop()

        backtrack(0, n)
        return parentheses