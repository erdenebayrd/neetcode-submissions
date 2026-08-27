import heapq

class MedianFinder:

    def __init__(self):
        self.decrease = [] #   * -1
        self.increase = []

    def addNum(self, num: int) -> None: # O(log N)
        if len(self.increase) < len(self.decrease): # add to increase
            if -self.decrease[0] <= num:
                heapq.heappush(self.increase, num)
            else:
                move = -heapq.heappop(self.decrease)
                heapq.heappush(self.increase, move)
                heapq.heappush(self.decrease, -num)
        else: # add to decrease
            if self.increase and self.increase[0] < num:
                move = heapq.heappop(self.increase)
                heapq.heappush(self.decrease, -move)
                heapq.heappush(self.increase, num)
            else:
                heapq.heappush(self.decrease, -num)

    def findMedian(self) -> float:
        if len(self.increase) == len(self.decrease):
            return (self.increase[0] - self.decrease[0]) / 2
        return -self.decrease[0]