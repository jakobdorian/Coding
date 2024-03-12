class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        res = 0  # length of the longest subarray with at most one zero
        left, right = 0, 0  # pointers for the sliding window
        count = 0  # count of zeros within the sliding window

        # iterate through the array
        while right < len(nums):
            if nums[right] == 0:
                count += 1  # increment count if the current element is zero

            # move the left pointer until count exceeds 1
            while count > 1:
                if nums[left] == 0:
                    count -= 1  # decrement count if the leftmost element is zero
                left += 1  # move the left pointer to shrink the window

            # update the result with the maximum length of the subarray
            res = max(res, right - left + 1)

            # move the right pointer to expand the window
            right += 1

        # adjust the result to account for the case when all elements are zeros
        if res > 0:
            return res - 1  # subtract 1 if the result is greater than 0
        else:
            return 0  # return 0 if there are no non-zero elements
