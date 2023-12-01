# O(n) sol
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        # go through each character looking for operators or nums
        for ch in tokens:
            if ch == "+":
                stack.append(stack.pop() + stack.pop())
            elif ch == "-":
                s1, s2 = stack.pop(), stack.pop()
                stack.append(s2 - s1)
            elif ch == "*":
                stack.append(stack.pop() * stack.pop())
            elif ch == "/":
                s1, s2 = stack.pop(), stack.pop()
                stack.append(int(s2 / s1))
            else:
                # convert num into an int before adding to stack
                stack.append(int(ch))
        return stack[0]
        