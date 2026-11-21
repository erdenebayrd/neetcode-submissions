class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # time: O(n)
        # space: O(1)
        # method: Greedy

        n = len(intervals)
        if n == 0 or intervals[-1][1] < newInterval[0]:
            intervals.append(newInterval)
            return intervals
        
        if newInterval[1] < intervals[0][0]:
            intervals.insert(0, newInterval)
            return intervals
        
        for i in range(1, n):
            if intervals[i - 1][1] < newInterval[0] and newInterval[1] < intervals[i][0]:
                intervals.insert(i, newInterval)
                return intervals

        # merge
        left = right = -1
        for i in range(n):
            if newInterval[0] <= intervals[i][1] and left == -1:
                left = i

            if left != -1 and intervals[i][0] <= newInterval[1]:
                right = i
        
        assert left != -1 and right != -1

        arr = intervals[:left] + [[min(intervals[left][0], newInterval[0]), max(intervals[right][1], newInterval[1])]] + intervals[right + 1:]
        return arr
