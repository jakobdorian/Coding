class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        # variable to store the count of flips needed
        res = 0
        
        # iterate until the 'c' number becomes 0
        while c > 0:
            # extract the least significant bit of 'c', 'a', and 'b'
            c1 = c % 2
            a1 = a % 2
            b1 = b % 2

            # check the conditions based on the least significant bits
            if c1 == 0:
                # if the least significant bit of 'c' is 0,
                # add the sum of least significant bits of 'a' and 'b' to 'res'
                res += a1 + b1
            elif a1 + b1 == 0:
                # if the least significant bits of 'a' and 'b' are both 0,
                # but the least significant bit of 'c' is 1,
                # add 1 to 'res'
                res += 1
            
            # right shift 'c', 'a', and 'b' by 1 bit
            c //= 2
            a //= 2
            b //= 2

        # after handling bits of 'c', if there are remaining bits in 'a', add them to 'res'
        while a > 0:
            if a % 2 == 1:
                res += 1
            a //= 2
            
        # after handling bits of 'c', if there are remaining bits in 'b', add them to 'res'
        while b > 0:
            if b % 2 == 1:
                res += 1
            b //= 2
        
        # return the total count of flips needed
        return res
