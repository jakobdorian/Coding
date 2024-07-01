class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        res = 0
        for num in arr:
            # check if num is odd
            if num % 2 != 0:
                res += 1
                # check if there are 3 consec odd nums
                if res == 3:
                    return True
            else:
                # reset counter
                res = 0
        return False
