# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        found = False
        i = 0
        res = []
        # iterate through the list looking at two items at a time
        while i < len(nums) and not found:
            j = i + 1
            while j < len(nums) and not found:
                # if the two items equal target then it is found
                if nums[i] + nums[j] == target:
                    found = True
                    res.append(i)
                    res.append(j)
                j += 1
            i += 1
        return res