class Solution:
    def removeStars(self, s: str) -> str:
        # an empty stack to store characters
        stack = []

        # iterate through each character in the input string
        for ch in s:
            # if the current character is "*", check if the stack is not empty
            if ch == "*":
                # and if it's not, pop the top element from the stack.
                stack and stack.pop()
            else:
                # if the current character is not "*", append it to the stack.
                stack.append(ch)

        # concatenate the characters in the stack to form the final string.
        return "".join(stack)
