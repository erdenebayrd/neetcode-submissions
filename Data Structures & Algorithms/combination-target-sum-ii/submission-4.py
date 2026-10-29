class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        n = len(candidates)

        combinations = []
        current = []

        def backtrack(index: int, target: int) -> None:
            if target == 0:
                combinations.append(current[:])
            
            if target <= 0 or index >= n:
                return
            
            # take
            current.append(candidates[index])
            backtrack(index + 1, target - candidates[index])
            current.pop()

            # skip
            next_index = index
            while next_index < n and candidates[index] == candidates[next_index]:
                next_index += 1
            
            backtrack(next_index, target)
        
        backtrack(0, target)
        return combinations