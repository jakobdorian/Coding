class Solution:
    def myPow(self, x: float, n: int) -> float:
        # recursive helper function to calculate power efficiently
        def helper(x, n):
            if x == 0:  # base case
                return 0
            if n == 0:  # base case
                return 1
            
            # recursively calculate power by dividing the exponent by 2 each time
            res = helper(x * x, n // 2)
            
            # if the exponent is odd, multiply the result by x
            if n % 2:
                return x * res
            else:  # if the exponent is even, return the result as is
                return res
            
        res = helper(x, abs(n))
        
        # if n is non-negative, return the result
        if n >= 0:
            return res
        else:  # if n is negative, return the reciprocal of the result
            return 1 / res

        # Time Complexity: O(log(n)), where n is the exponent
        # Space Complexity: O(log(n)), due to the recursive call stack
        