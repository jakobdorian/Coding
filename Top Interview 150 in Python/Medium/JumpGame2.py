# greedy approach using a BFS to find min jumps
class Solution:
    def jump(self, nums: List[int]) -> int:
        res, p1, p2 = 0, 0, 0
        # search array until the 2nd pointer reaches the last index
        while p2 < len(nums) - 1:
            max_jump = 0
            for i in range(p1, p2 + 1):
                # what is the furthest we can jump to?
                max_jump = max(max_jump, i + nums[i])
            # update current window / pointers
            p1 = p2 + 1
            p2 = max_jump
            res += 1
        return res