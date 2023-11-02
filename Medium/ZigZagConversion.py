class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # already completed
        if numRows == 1:
            return s
        
        res = []
        # go through each row
        for r in range(numRows):
            count = 2 * (numRows - 1)
            # first and last row
            for i in range(r, len(s), count):
                res.append(s[i])
                # middle rows
                if (r > 0 and r < numRows - 1 and i + count - 2 * r < len(s)):
                    res.append(s[i + count - 2 * r])
        # convert list back into a string then return
        return ''.join([str(elem) for elem in res])
