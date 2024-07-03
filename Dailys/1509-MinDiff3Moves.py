class Solution:
    def minDifference(self, nums: List[int]) -> int:
        # if the length of the list is 4 or less, the minimum difference is 0
        if len(nums) <= 4:
            return 0

        # find the four smallest elements in the list
        min_four = sorted(heapq.nsmallest(4, nums))
        # find the four largest elements in the list
        max_four = sorted(heapq.nlargest(4, nums))

        # initialize the result with infinity
        res = float("inf")

        # compare the difference between the i-th largest and i-th smallest element
        for i in range(4):
            res = min(res, max_four[i] - min_four[i])
        
        # return the minimum difference found
        return res
        