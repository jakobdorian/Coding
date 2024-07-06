class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        # if n is 1, there's only one person, so they always have the pillow.
        if n == 1:
            return 1
    
        # the effective time considering the round trip of the pillow.
        effective_time = time % (2 * n - 2)
    
        # if the effective time is less than n, it's still in the first pass.
        if effective_time < n:
            return effective_time + 1
        else:
            # otherwise, it's in the return pass.
            return 2 * n - 1 - effective_time
