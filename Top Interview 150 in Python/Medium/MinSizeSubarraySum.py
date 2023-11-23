class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        p1 = 0
        sum = 0
        res = float("inf")
        for p2 in range(len(nums)):
            # add val to total
            sum += nums[p2]
            while sum >= target:
                res = min(p2 - p1 + 1, res)
                sum -= nums[p1]
                p1 += 1
        if res == float("inf"):
            return 0
        else:
            return res
            