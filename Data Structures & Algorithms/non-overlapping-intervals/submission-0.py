class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # time: O(n log n)
        # space: O(n) # due to timsort
        # method: Greedy

        n = len(intervals)
        if n <= 1:
            return 0

        intervals.sort()
        # print(intervals)
        count = 0
        prev_left, prev_right = intervals[0]
        for i in range(1, n):
            curr_left, curr_right = intervals[i]

            if prev_right <= curr_left: # non overlap
                prev_left, prev_right = curr_left, curr_right
            else: # prev_right >= curr_left overlap 
                count += 1
                if prev_right > curr_right: # delete prev one
                    prev_left, prev_right = curr_left, curr_right
        return count
