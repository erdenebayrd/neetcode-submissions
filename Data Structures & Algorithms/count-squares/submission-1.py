from collections import defaultdict

class CountSquares:

    def __init__(self):
        self.counts = defaultdict(int)

    def add(self, point: List[int]) -> None:
        self.counts[tuple(point)] += 1

    def count(self, point: List[int]) -> int:
        query_x, query_y = point
        total = 0
        for x, y in self.counts:
            if x == query_x or y == query_y or abs(x - query_x) != abs(y - query_y):
                continue
            if (x, query_y) not in self.counts or (query_x, y) not in self.counts:
                continue
                
            total += self.counts[(x, query_y)] * self.counts[(query_x, y)]

        return total