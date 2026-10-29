class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        n = len(candidates)

        seen = set()
        current = []
        combinations = []
        def recursive(target: int, index: int, length: int) -> None:
            if target == 0:
                combinations.append(current[:])
                return

            state = (target, index, length)
            if target < 0 or index >= n or state in seen:
                return

            seen.add(state)

            recursive(target, index + 1, length)

            current.append(candidates[index])
            recursive(target - candidates[index], index + 1, length + 1)
            current.pop()
        
        recursive(target, 0, 0)
        return combinations