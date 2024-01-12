class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0    
        while n:
            # increment the count if the rightmost bit is 1.
            res += n % 2
            # right shift n by 1 to move to the next bit.
            n = n >> 1
        return res
        