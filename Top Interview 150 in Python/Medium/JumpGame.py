# greedy O(n) solution
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        last_index = len(nums) - 1
        # work backwards through the array
        for i in range(len(nums) -1, -1, -1):
            # check if we can jump the last index
            if i + nums[i] >= last_index:
                last_index = i
        if last_index == 0:
            return True
        else:
            return False