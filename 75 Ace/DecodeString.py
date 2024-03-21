class Solution:
    def decodeString(self, s: str) -> str:
        # an empty list to store characters
        res = []
        # iterate through each character in the input string
        for i in range(len(s)):
            if s[i] != "]":
                res.append(s[i])
            else:
                sub = ""
                # keep popping characters until an opening bracket is encountered
                while res[-1] != "[":
                    sub = res.pop() + sub
                res.pop()
            
                k = ""
                # keep popping characters while they are digits
                while res and res[-1].isdigit():
                    k = res.pop() + k
                # append the substring repeated k times to the result list
                res.append(int(k) * sub) 
        # convert the result list to a string and return
        return "".join(res)
