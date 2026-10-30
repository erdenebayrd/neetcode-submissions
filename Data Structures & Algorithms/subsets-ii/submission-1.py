class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # time: O(n * 2 ^ n)
        # space: O(n * 2 ^ n)
        # method: backtrack/bitmask
        arr = sorted(nums)
        n = len(nums)
        subsets = []
        current = []
        
        def backtrack(index: int) -> None:
            if index >= n:
                subsets.append(current[:])
                return
            
            # take
            current.append(arr[index])
            backtrack(index + 1)
            current.pop()

            # skip
            while index + 1 < n and arr[index] == arr[index + 1]:
                index += 1
            
            backtrack(index + 1)
        
        backtrack(0)
        return subsets