def palindromeIndex(s):
    # helper function to check if a string is a palindrome
    def helper(s):
        return s == s[::-1]
    
    # if the entire string is already a palindrome, return -1
    if helper(s):
        return -1
    
    n = len(s)
    
    # iterate over the first half of the string
    for i in range(n // 2):
        # if characters at the current position and its mirror position do not match
        if s[i] != s[n - i - 1]:
            # check if removing the character at position i makes the string a palindrome
            if helper(s[i+1:n - i]):
                return i  # return the index of the removed character
            # check if removing the character at the mirror position makes the string a palindrome
            elif helper(s[i:n - i - 1]):
                return n - i - 1  # return the index of the removed character (mirror position)
    
    # if no single character removal can make the string a palindrome, return -1
    return -1
