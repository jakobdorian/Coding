class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        # calculate the integer square root of c
        sq = int(sqrt(c))

        # iterate through all possible values of a from 0 to the square root of c
        for a in range(sq + 1):
            # calculate the value of b such that a^2 + b^2 = c
            b = sqrt(c - (a * a))
            # check if b is an integer
            if b == int(b):
                # if b is an integer, return True because a^2 + b^2 = c
                return True
        # if no such pair (a, b) is found, return False
        return False
