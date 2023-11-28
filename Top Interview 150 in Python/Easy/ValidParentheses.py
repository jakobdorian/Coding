class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        lookup = {")" : "(", "]" : "[", "}" : "{"}
        # go through strings
        for ch in s:
            # check if current char is a closing
            if ch in lookup:
                if stack and stack[-1] == lookup[ch]:
                    stack.pop()
                # does not match or is empty
                else:
                    return False
            else:
                stack.append(ch)
        if not stack:
            return True
        else:
            return False
