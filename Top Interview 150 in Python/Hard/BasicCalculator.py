# O(n) sol
class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        res, curr, op = 0, 0, 1

        for ch in s:
            # digit
            if ch.isdigit():
                curr = curr * 10 + int(ch)
            # +=
            elif ch in "+-":
                res += (curr * op)
                curr = 0
                if ch == "-":
                    op = -1
                else:
                    op = 1
            # (
            elif ch == "(":
                stack.append(res)
                stack.append(op)
                res = 0
                op = 1
            # )
            elif ch == ")":
                res += (curr * op)
                res *= stack.pop()
                res += stack.pop()
                curr = 0
        return res + (curr * op)
