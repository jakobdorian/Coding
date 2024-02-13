class Solution:
    def trailingZeroes(self, n: int) -> int:
        # if n is less than 5, it means there are no trailing zeros, return 0
        if n < 5:
            return 0
        res = 0
        # variable to iterate through multiples of 5
        i = 5

        # iterate until n divided by i is not equal to 0
        while n // i != 0:
            # add the count of multiples of i (which represent the number of trailing zeros) to the result
            res += n // i
            # multiply i by 5 to move to the next multiple
            i *= 5
        # return the total count of trailing zeros
        return res
