class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed))
        stack = [] # contains tuple (distance, speed)
        n = len(cars)
        for i in range(n - 1, -1, -1):
            position, speed = cars[i]
            distance = target - position
            if not stack:
                stack.append((distance, speed))
            elif stack:
                prev_distance, prev_speed = stack[-1]
                if distance * prev_speed > prev_distance * speed:
                    stack.append((distance, speed))
        return len(stack)