class Solution:
    def reverseBits(self, n: int) -> int:
        # initialize variables: res to store the reversed bits, power for bit position
        res, power = 0, 31
        while n:
            # extract the last bit of n using bitwise AND with 1, then left shift it to the correct position
            res += (n & 1) << power
            # right shift n to move to the next bit
            n = n >> 1
            # decrease the power (bit position) for the next iteration
            power -= 1
        return res
