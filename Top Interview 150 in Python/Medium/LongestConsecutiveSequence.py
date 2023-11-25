# O(n), O(n) sol
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # change the array into a set
        numSet = set(nums)
        # longest consecutive sequence
        res = 0
        length = 0

        for n in nums:
            # check if its the start of a sequence
            if (n - 1) not in numSet:
                while (n + length) in numSet:
                    length += 1
                res = max(length, res)
        return res
