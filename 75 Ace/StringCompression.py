class Solution:
    def compress(self, chars: List[str]) -> int:
        # check if the input list is empty
        if not chars:
            return 0
        
        # variables for result and count of characters
        res = 0
        count = 1

        # iterate through the characters starting from the second one
        for i in range(1, len(chars)):
            # if the current character is the same as the previous one, increment count
            if chars[i] == chars[i - 1]:
                count += 1
            else:
                # if the current character is different, update the character at res index
                chars[res] = chars[i - 1]
                res += 1
                # if count is greater than 1, convert it to string and append its digits to chars
                if count > 1:
                    for digit in str(count):
                        chars[res] = digit
                        res += 1
                # reset count for the new character
                count = 1

        # update the last character in chars and its count if greater than 1
        chars[res] = chars[-1]
        res += 1
        if count > 1:
            for digit in str(count):
                chars[res] = digit
                res += 1

        # return the length of the compressed list
        return res
