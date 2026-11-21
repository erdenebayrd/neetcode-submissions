"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # time: O(n + R) R max end value across all intervals
        # space: O(R)
        # method: Greedy
        n = len(intervals)
        if n <= 0:
            return 0
        high = max([item.end for item in intervals])
        rooms = [0] * (high + 1)
        for item in intervals:
            rooms[item.start] += 1
            rooms[item.end] -= 1
        
        for current in range(1, high + 1):
            rooms[current] += rooms[current - 1]

        return max(rooms)