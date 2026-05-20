class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for ch in tokens:
            if ch == "+":
                value = stack.pop()
                stack[-1] += value
            elif ch == "-":
                value = stack.pop()
                stack[-1] -= value
            elif ch == "*":
                value = stack.pop()
                stack[-1] *= value
            elif ch == "/":
                value = stack.pop()
                stack[-1] = int(stack[-1] / value)
            else:
                stack.append(int(ch))
        return stack[0]