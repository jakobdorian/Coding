class Solution:
    def reverseVowels(self, s: str) -> str:
        # set of vowels to be checked against
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        
        # convert string to list for easier swapping of characters
        s = list(s)
        
        # pointers for traversing string from both ends
        i, j = 0, len(s) - 1
    
        # loop until the pointers meet
        while i < j:
            # uf both characters at pointers are vowels, swap them
            if s[i] in vowels and s[j] in vowels:
                s[i], s[j] = s[j], s[i]
                i += 1
                j -= 1
            # if only character at index i is vowel, move j towards start
            elif s[i] in vowels:
                j -= 1
            # if only character at index j is vowel, move i towards end
            elif s[j] in vowels:
                i += 1
            # if neither character is vowel, move both pointers towards each other
            else:
                i += 1
                j -= 1
        
        # convert the list back to string and return
        return ''.join(s)
