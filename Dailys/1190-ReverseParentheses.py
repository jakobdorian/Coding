class Solution:
    def reverseParentheses(self, s: str) -> str:
        res = []
        for ch in s:
            if ch == ")":
                temp = []
                # pop from stack until matching '(' is found
                while res and res[-1] != '(':
                    temp.append(res.pop())
                # pop the '('
                if res:
                    res.pop()
                # push the reversed substring back to the stack
                res.extend(temp)
            else:
                res.append(ch)
        # join all characters to form the resulting string
        return ''.join(res)
