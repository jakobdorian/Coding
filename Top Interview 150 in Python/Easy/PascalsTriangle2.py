# Given an integer rowIndex, return the row Indexth (0-indexed) row of the Pascal's triangle.
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        # first row
        res = [1]
        for i in range(rowIndex):
            # next row
            next = [0] * (len(res) + 1)
            # iterate over values in previous row
            for j in range(len(res)):
                # add the value to the child index +1
                next[j] += res[j]
                next[j+1] += res[j]
            res = next
        return res