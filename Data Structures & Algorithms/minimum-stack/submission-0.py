class MinStack:

    def __init__(self):
        self.monotonic_nonincreasing_stack = []
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.monotonic_nonincreasing_stack or self.monotonic_nonincreasing_stack[-1] >= val:
            self.monotonic_nonincreasing_stack.append(val)

    def pop(self) -> None:
        value = self.stack.pop()
        if self.monotonic_nonincreasing_stack[-1] == value:
            self.monotonic_nonincreasing_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.monotonic_nonincreasing_stack[-1]
