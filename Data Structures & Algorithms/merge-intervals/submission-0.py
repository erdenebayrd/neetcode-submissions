class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # time: O(n log n)
        # space: O(n) due to timsort and output array
        # method: sorting + greedy
        n = len(intervals)
        if n <= 1:
            return intervals

        intervals.sort()
        result = [intervals[0]]
        for i in range(1, n):
            if result[-1][1] < intervals[i][0]:
                result.append(intervals[i])
            else: # overlap  result[-1][1] >= intervals[i][0]:
                result[-1][1] = max(result[-1][1], intervals[i][1])
        return result