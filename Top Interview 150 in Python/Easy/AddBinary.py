class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # convert binary strings to integers and add them
        res = int(a, 2) + int(b, 2)
        # convert the result back to binary and return as a string
        return "{:b}".format(res)
        