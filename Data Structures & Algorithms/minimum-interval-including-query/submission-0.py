import heapq

class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        # time: O((n + m) * log n) n is len of intervals, m is len of queries
        # space: O(n + m)
        # method: min heap + lazy deletion + sorting
        
        n = len(intervals)
        intervals.sort()
        
        m = len(queries)
        queries_sorted = []
        for i in range(m):
            queries_sorted.append((queries[i], i))
        
        result = [-1] * m
        queries_sorted.sort()
        
        min_heap_right_length = [] # right, length
        min_heap_length_right = [] # length, right
        lazy_delete = set()

        right = 0
        for point, index in queries_sorted:
            while right < n and intervals[right][0] <= point:
                heapq.heappush(min_heap_right_length, (intervals[right][1], intervals[right][1] - intervals[right][0] + 1))
                heapq.heappush(min_heap_length_right, (intervals[right][1] - intervals[right][0] + 1, intervals[right][1]))
                right += 1
            
            while min_heap_right_length and min_heap_right_length[0][0] < point: # removing non overlapped intervals
                interval_right, interval_length = heapq.heappop(min_heap_right_length)
                lazy_delete.add((interval_length, interval_right))
            
            while min_heap_length_right and min_heap_length_right[0] in lazy_delete:
                heapq.heappop(min_heap_length_right)
            
            if min_heap_length_right:
                result[index] = min_heap_length_right[0][0]
        
        return result