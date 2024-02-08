class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # total number of elements in both arrays
        total = len(nums1) + len(nums2)
        # index that divides the two arrays to get the median
        half = total // 2

        # ensure nums1 is the shorter array for efficient partitioning
        if len(nums2) < len(nums1):
            nums1, nums2 = nums2, nums1

        # pointers for binary search
        left, right = 0, len(nums1) - 1
        # binary search
        while True:
            mid1 = (left + right) // 2
            mid2 = half - mid1 - 2

            # calculate left and right elements for both arrays
            left1 = nums1[mid1] if mid1 >= 0 else float("-infinity")
            right1 = nums1[mid1 + 1] if (mid1 + 1) < len(nums1) else float("infinity")
            left2 = nums2[mid2] if mid2 >= 0 else float("-infinity")
            right2 = nums2[mid2 + 1] if (mid2 + 1) < len(nums2) else float("infinity")

            # check if the partition is correct
            if left1 <= right2 and left2 <= right1:
                # if total number of elements is odd, return the smaller of right1 and right2
                if total % 2:
                    return min(right1, right2)
                # if total number of elements is even, return the average of the max of left1 and left2
                # and the min of right1 and right2
                else:
                    return (max(left1, left2) + min(right1, right2)) / 2
            # adjust pointers based on partition
            elif left1 > right2:
                right = mid1 - 1
            else:
                left = mid1 + 1
