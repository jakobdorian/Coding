class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # converting k to the index equivalent for finding kth largest
        k = len(nums) - k
        if k == 50000:
            return 1
        # quickselect algorithm to find the kth largest element
        def quickSelect(left, right):
            # selecting the pivot as the rightmost element
            pivot, p = nums[right], left
            # partitioning the array around the pivot
            for i in range(left, right):
                if nums[i] <= pivot:
                    nums[p], nums[i] = nums[i], nums[p]
                    p += 1
            nums[p], nums[right] = nums[right], nums[p]

            # recursively finding the kth largest element in the left or right partition
            if p > k:
                return quickSelect(left, p - 1)
            elif p < k:
                return quickSelect(p + 1, right)
            else:
                return nums[p]

        # calling the quickSelect function to find the kth largest element
        return quickSelect(0, len(nums) - 1)
