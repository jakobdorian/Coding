class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        # define a helper function that will be used recursively
        def helper(n, k):
            # base case: if there is only one person left, return 0 (the position of the winner in zero-indexed form)
            if n == 1:
                return 0
            
            # recursively call helper to find the position of the winner with one less person
            # the position of the winner is adjusted by k and taken modulo n to wrap around if necessary
            return (helper(n - 1, k) + k) % n
        
        # the winner's position in one-indexed form is obtained by adding 1 to the zero-indexed result from helper
        return helper(n, k) + 1
