class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # time: O(n * n!) = O(n!)
        # space: O(n!)
        # method: brute force
        nums.sort() # O(n log n)

        def get_next_permutation(arr: list) -> list: # O(n)
            index = -1
            for i in range(len(arr) - 1, 0, -1):
                current = arr[i]
                prev = arr[i - 1]
                if prev < current:
                    index = i - 1
                    break
            
            if index == -1:
                return []
            
            for i in range(len(arr) - 1, -1, -1):
                if arr[i] > arr[index]:
                    # swap
                    arr[i], arr[index] = arr[index], arr[i]
                    break
            
            first_half = arr[:index + 1]
            second_half = arr[index + 1:]
            next_permutation = first_half + second_half[::-1]
            return next_permutation

            
        next_permutation = nums[:]
        permutations = [next_permutation[:]]
        while next_permutation:=get_next_permutation(next_permutation):
            permutations.append(next_permutation[:])
        
        return permutations