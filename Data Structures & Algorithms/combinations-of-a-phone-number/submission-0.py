class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # time: O(3 ^ n)
        # space: O(3 ^ n)
        # method: backtrack

        char_map = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        
        combs = []
        current = []
        n = len(digits)

        def backtrack(index: int) -> None:
            if index >= n:
                if current:
                    combs.append("".join(current))
                return
            
            for ch in char_map[digits[index]]:
                current.append(ch)
                backtrack(index + 1)
                current.pop()
        
        backtrack(0)
        return combs