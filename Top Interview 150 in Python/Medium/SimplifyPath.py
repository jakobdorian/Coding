class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        # current path
        curr = ""

        for ch in path + "/":
            # check if the current ch is a "/"
            if ch == "/":
                if curr == "..":
                    if stack:
                        stack.pop()
                # if current is not empty, and is not a dot
                elif curr != "" and curr != ".":
                    stack.append(curr)
                # reset variables
                curr = ""
            else:
                curr += ch
        # build simplfy path, then return
        return "/" + "/".join(stack)
        