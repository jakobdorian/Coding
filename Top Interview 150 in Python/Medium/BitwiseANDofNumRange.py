class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        # track the number of right shifts needed
        shift = 0
        # continue right-shifting both left and right until they are equal
        while left != right:
            left >>= 1
            right >>= 1
            shift += 1
        # left shift the final value to reconstruct the common prefix
        return left << shift
        