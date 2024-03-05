class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        # two variables to store the smallest and second smallest elements seen so far.
        first = second = float("inf")
        
        # iterate through the list of numbers.
        for n in nums:
            # if the current number is smaller than or equal to the smallest seen so far,
            # update the smallest seen so far to the current number.
            if n <= first:
                first = n
            # if the current number is greater than the smallest but smaller than or equal
            # to the second smallest seen so far, update the second smallest seen so far to the current number.
            elif n <= second:
                second = n
            # if the current number is greater than both the smallest and second smallest seen so far,
            # we have found an increasing triplet, return True.
            else:
                return True
        
        # if no increasing triplet is found, return False.
        return False
