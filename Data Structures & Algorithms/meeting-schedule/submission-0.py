"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

from functools import cmp_to_key

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        # time: O(n log n) n is len of intervals
        # space: O(n) due to timsort
        # method: Greedy
        n = len(intervals)
        if n <= 1:
            return True
        
        def compare(a: Interval, b: Interval) -> int:
            if a.start < b.start:
                return -1
            elif a.start > b.start:
                return 1
            
            if a.end < b.end:
                return -1
            elif a.end > b.end:
                return 1
            
            return 0

        intervals.sort(key=cmp_to_key(compare))

        for i in range(1, n):
            if intervals[i - 1].end > intervals[i].start:
                return False
        return True