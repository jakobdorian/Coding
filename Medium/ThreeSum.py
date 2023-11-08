# O(n2) time sol 
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        # sort array
        nums.sort()
        for i, a in enumerate(nums):
            # same value as before
            if i > 0 and a == nums[i - 1]:
                continue
            # two sum
            p1, p2 = i + 1, len(nums) - 1
            while p1 < p2:
                threeSum = a + nums[p1] + nums[p2]
                if threeSum > 0:
                    p2 -= 1
                elif threeSum < 0:
                    p1 += 1
                else:
                    res.append([a, nums[p1], nums[p2]])
                    # update pointers
                    p1 += 1
                    # is is the same val?
                    while nums[p1] == nums[p1 - 1] and p1 < p2:
                        p1 += 1
        return res
