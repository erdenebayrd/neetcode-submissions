class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed))
        stack = []
        n = len(cars)
        for i in range(n - 1, -1, -1):
            position, speed = cars[i]
            distance = target - position
            hours = distance / speed
            if not stack or hours > stack[-1]:
                stack.append(hours)
        return len(stack)