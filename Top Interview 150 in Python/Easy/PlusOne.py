class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # convert the list of digits to an integer, add 1, and convert back to a list of digits
        res = int("".join([str(i) for i in digits])) + 1
        # convert the result to a list of digits
        return [int(i) for i in str(res)]
