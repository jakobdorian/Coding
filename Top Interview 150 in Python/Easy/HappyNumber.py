class Solution:
    def isHappy(self, n: int) -> bool:
        # hashset to keep track of numbers visted
        visited = set()

        while n not in visited:
            # add n if not visited
            visited.add(n)
            # compute happy process
            n = self.happyProcess(n)
            # condition met
            if n == 1:
                return True
        return False
    # helper function to process if a num is happy or not
    def happyProcess(self, n: int) -> int:
        output = 0
        # loop until n == 0
        while n:
            digit = n % 10
            digit = digit ** 2
            output += digit
            n = n // 10
        return output
            