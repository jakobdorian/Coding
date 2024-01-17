class Solution:
    def mySqrt(self, x: int) -> int:
        left, right = 0, x
        res = 0 
        # binary search loop
        while left <= right:
            mid = left + ((right - left) // 2)  # calculate the middle point
            # check if the square of mid is greater than x
            if mid**2 > x:
                right = mid - 1  # adjust the search range to the left
            # check if the square of mid is less than x
            elif mid**2 < x:
                left = mid + 1  # adjust the search range to the right
                res = mid  # update the result to the current mid
            else:
                return mid  # return mid if its square is exactly x
        return res
