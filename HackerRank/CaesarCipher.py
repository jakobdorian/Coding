def caesarCipher(s, k):
    res = []
    # ensure that the shift k is within the range of 0-25 by taking k modulo 26
    k = k % 26
    
    # iterate through each character in the input string s
    for char in s:
        # check if the character is a lowercase letter
        if 'a' <= char <= 'z':
            # shift the character by k positions within the lowercase alphabet
            new_char = chr((ord(char) - ord('a') + k) % 26 + ord('a'))
        # check if the character is an uppercase letter
        elif 'A' <= char <= 'Z':
            # shift the character by k positions within the uppercase alphabet
            new_char = chr((ord(char) - ord('A') + k) % 26 + ord('A'))
        else:
            # if the character is neither uppercase nor lowercase, leave it unchanged
            new_char = char
        
        # append the new character to the result list
        res.append(new_char)
    
    # join the list of characters into a single string and return it
    return ''.join(res)
