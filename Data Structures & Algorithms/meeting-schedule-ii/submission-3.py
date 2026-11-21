"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # # time: O(n + R) R max end value across all intervals
        # # space: O(R)
        # # method: Greedy
        # n = len(intervals)
        # if n <= 0:
        #     return 0
        # high = max([item.end for item in intervals])
        # rooms = [0] * (high + 1)
        # for item in intervals:
        #     rooms[item.start] += 1
        #     rooms[item.end] -= 1
        
        # for current in range(1, high + 1):
        #     rooms[current] += rooms[current - 1]

        # return max(rooms)

        # coordinate compression not dependent of big values
        # time: O(n log n)
        # space: O(n)
        # method: coordinate compression
        
        n = len(intervals)
        if n <= 0:
            return 0
        values = set()
        for item in intervals:
            values.add(item.start)
            values.add(item.end)
        
        values = sorted(values)
        values_map = {}
        for i in range(len(values)):
            values_map[values[i]] = i
        
        rooms = [0] * len(values)
        for item in intervals:
            start_value = values_map[item.start]
            end_value = values_map[item.end]
            rooms[start_value] += 1
            rooms[end_value] -= 1
        
        for i in range(1, len(rooms)):
            rooms[i] += rooms[i - 1]
        
        return max(rooms)
        







