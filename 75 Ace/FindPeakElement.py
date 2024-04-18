class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left, right = 0, len(nums)-1
        # binary search loop
        while left < right:
            mid = (left + right) // 2
            # check if the peak is on the right side
            if nums[mid] < nums[mid+1]:
                left = mid + 1
            # check if the peak is on the left side or current element is the peak
            else:
                right = mid
        # left pointer is the index of the peak element
        return left
