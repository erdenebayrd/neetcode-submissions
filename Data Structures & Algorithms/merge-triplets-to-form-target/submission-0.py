class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        # time: O(n) n is len of triplets array
        # space: O(1)
        # method: Greedy
        inf = float('inf')
        current = [-inf, -inf, -inf]
        n = len(triplets)
        for i in range(n):
            for j in range(3):
                if triplets[i][j] > target[j]:
                    break
            else:
                for j in range(3):
                    current[j] = max(current[j], triplets[i][j])

        for i in range(3):
            if current[i] != target[i]:
                return False
        return True