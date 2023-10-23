# O(n) time complexity
# Given an array of integers citations where citations[i] is the number of citations a researcher received for their ith paper, return the researcher's h-index.
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        # create a temporary array
        temp = [0 for _ in range(n+1)]
        # go through citations
        for p1, p2 in enumerate(citations):
            # is the current element bigger than the length?
            if p2 > n:
                temp[n] += 1
            else:
                temp[p2] += 1
        total = 0
        # move backwards through the array
        for i in range(n, -1, -1):
            total += temp[i]
            if total >= i:
                return i