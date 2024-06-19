def isBalanced(s):
    stack = []
    
    # dictionary to map closing brackets to their corresponding opening brackets
    b_map = {')': '(', '}': '{', ']': '['}
    
    # iterate over each character in the input string
    for char in s:
        # if the character is one of the opening brackets, push it onto the stack
        if char in b_map.values():
            stack.append(char)
        # if the character is one of the closing brackets
        elif char in b_map.keys():
            # check if the stack is empty or if the top element of the stack
            # does not match the corresponding opening bracket
            if stack == [] or b_map[char] != stack.pop():
                # if so, the string is not balanced
                return 'NO'
        # if the character is neither an opening nor a closing bracket
        else:
            # return 'YES' as the presence of non-bracket characters is not
            # relevant to the balance check
            return 'YES'
    
    # after processing all characters, check if the stack is empty
    # if the stack is empty, all opening brackets had matching closing brackets
    # if the stack is not empty, some opening brackets were not closed
    return 'YES' if stack == [] else 'NO'
