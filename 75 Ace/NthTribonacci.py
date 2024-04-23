class Solution:
    def tribonacci(self, n: int) -> int:
        # the first three elements of the tribonacci sequence
        t = [0, 1, 1]

        # if n is less than 3, return the corresponding element from the initial sequence
        if n < 3:
            return t[n]

        # generating the Tribonacci sequence up to the nth element
        for i in range(3, n + 1):
            # updating the elements of the sequence according to the tribonacci recurrence relation
            t[0], t[1], t[2] = t[1], t[2], sum(t)

        # returning the nth element of the tribonacci sequence
        return t[2]
