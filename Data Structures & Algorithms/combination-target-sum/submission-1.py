class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        current = []
        n = len(nums)
        def backtrack(index: int):
            if sum(current) > target:
                return

            if index == n:
                if sum(current) == target:
                    result.append(current[:])
                return
            
            backtrack(index + 1) # skip
            current.append(nums[index])
            backtrack(index)
            current.pop()
        
        backtrack(0)

        return result