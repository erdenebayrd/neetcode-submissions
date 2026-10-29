class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        n = len(candidates)
        seen = set()
        current = []

        def backtrack(index: int, target: int) -> None:
            if target == 0:
                seen.add(tuple(current[:]))
                return
                
            if index >= n or target < 0:
                return
            
            backtrack(index + 1, target)
            current.append(candidates[index])
            backtrack(index + 1, target - candidates[index])
            current.pop()
        
        backtrack(0, target)
        
        combinations = []
        for item in seen:
            combinations.append(list(item))
        
        return combinations