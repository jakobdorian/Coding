# Given an integer x, return true if x is a palindrome, and false otherwise.
class Solution:
    def isPalindrome(self, x: int) -> bool:
        # check if num is negative
        if x < 0: 
            return False
        temp = 1
        while x >= 10 * temp:
            temp *= 10
        while x:
            # take off the right and left sides of the number
            r = x % 10
            l = x // temp
            
            # check if the left side is equal to the right side
            if l != r:
                return False
            x = (x % temp) // 10
            temp = temp / 100
        return True