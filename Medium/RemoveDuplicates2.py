class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # left pointer
        p1 = 0
        # right pointer
        p2 = 0
        while p2 < len(nums):
            curr = 1
            # track the current streak of duplicates
            while p2 + 1 < len(nums) and nums[p2] == nums[p2 + 1]:
                p2 += 1
                curr += 1
            # get the minimum value and place it in the correct index
            for i in range(min(2, curr)):
                nums[p1] = nums[p2]
                p1 += 1
            p2 += 1
        return p1
