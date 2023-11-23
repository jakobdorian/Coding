# Given an array nums of size n, return the majority element.
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        res = 0
        # majority = 0
        # O(1) space complexity
        for i in nums:
            if count == 0:
                res = i
            count += (1 if i == res else - 1)
        return res

        # for i in nums:
        #     count[i] = 1 + count.get(i, 0)
        #     # if the current count is greater then majority
        #     res = if count[i] > majority else res
        #     majority = max(count[i], majority)
        # return res

