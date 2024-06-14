class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        # sort the heights to get the expected order
        expected = sorted(heights)
        
        # a counter for mismatched positions
        res = 0

        # iterate through each index in the list
        for i in range(len(heights)):
            # compare the original height with the expected height
            if heights[i] != expected[i]:
                # increment the counter if there is a mismatch
                res += 1
        
        # return the total number of mismatches
        return res
