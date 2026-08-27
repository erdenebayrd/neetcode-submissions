from sortedcontainers import SortedList

class MedianFinder:

    def __init__(self):
        self.sl = SortedList()        

    def addNum(self, num: int) -> None: # O(log N)
        self.sl.add(num)

    def findMedian(self) -> float:
        if len(self.sl) & 1:
            return self.sl[len(self.sl) // 2]
        return (self.sl[len(self.sl) // 2] + self.sl[len(self.sl) // 2 - 1]) / 2
        