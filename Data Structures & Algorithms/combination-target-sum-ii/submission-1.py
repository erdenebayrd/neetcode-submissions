class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = set()
        current = []
        n = len(candidates)

        def backtrack(index: int):
            if sum(current) > target:
                return
            
            if index == n:
                if sum(current) == target:
                    result.add(tuple(current[:]))
                return
            
            backtrack(index + 1)

            current.append(candidates[index])
            backtrack(index + 1)
            current.pop()
        
        backtrack(0)

        
        result = [list(item) for item in result]
        return result