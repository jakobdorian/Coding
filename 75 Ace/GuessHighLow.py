class Solution:
    def guessNumber(self, n: int) -> int:
        left, right = 1, n

        # binary search loop
        while True:
            # calculate the mid point
            mid = (left + right) // 2
            res = guess(mid)
            
            # if guess is higher than the actual number, adjust the right boundary
            if res > 0:
                left = mid + 1
            # if guess is lower than the actual number, adjust the left boundary
            elif res < 0:
                right = mid - 1
            # if guess is correct, return the guessed number
            else:
                return mid
