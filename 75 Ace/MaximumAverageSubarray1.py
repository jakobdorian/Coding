class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        # initialize res to the sum of the first k elements of nums
        res = sum(nums[:k])
        # set curr to res initially
        curr = res

        # loop through the remaining elements of 'nums' starting from index 'k'
        for i in range(k, len(nums)):
            # update 'curr' by adding the current element and subtracting the element
            # that is 'k' positions behind the current element
            curr += nums[i] - nums[i-k]
            # update 'res' to the maximum between 'res' and 'curr'
            res = max(res, curr)

        # return the maximum average by dividing 'res' by 'k'
        return res / k
