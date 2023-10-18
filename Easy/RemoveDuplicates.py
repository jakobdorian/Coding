class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # left pointer
        res = 1
        # i is the right pointer
        for i in range(1, len(nums)):
            # checks if the current element is unique
            if nums[i] != nums[i - 1]:
                nums[res] = nums[i]
                # move up the list
                res += 1
        return res