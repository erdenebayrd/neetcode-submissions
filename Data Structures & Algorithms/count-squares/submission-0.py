from collections import defaultdict

class CountSquares:

    def __init__(self):
        self.counts = defaultdict(int)
        self.points = defaultdict(list)

    def add(self, point: List[int]) -> None:
        x, y = point
        self.counts[(x, y)] += 1
        self.points[x].append(y)

    def count(self, point: List[int]) -> int:
        query_x, query_y = point
        total = 0
        for y in self.points[query_x]:
            dist = abs(y - query_y)
            if dist == 0:
                continue

            for delta_x in (-1, 1):
                other_x = query_x + delta_x * dist
                total += self.counts[(other_x, y)] * self.counts[(other_x, query_y)]

        return total