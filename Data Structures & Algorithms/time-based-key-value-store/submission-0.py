from collections import defaultdict

class TimeMap:

    def __init__(self):
        self.store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store or timestamp < self.store[key][0][1]:
            return ""
        low, high = -1, len(self.store[key])
        while low + 1 < high:
            mid = (low + high) // 2
            if self.store[key][mid][1] <= timestamp:
                low = mid
            else:
                high = mid
        return self.store[key][low][0]