class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # get the length of the input array
        N = len(nums)
        # finding the pivot point using binary search
        left, right = 0, N - 1  
        while left < right:  
            mid = (left + right) // 2  # calculate the middle index  # O(1)
            if nums[mid] > nums[right]:  # check if the pivot is in the right half  # O(1)
                left = mid + 1  # move the search range to the right  # O(1)
            else:
                right = mid  # move the search range to the left  # O(1)

        pivot = left  # index where the array is rotated  # O(1)

        # binary search on the appropriate subarray
        left, right = 0, N - 1  # reset the search range  # O(1)
        while left <= right:  # perform binary search on the rotated array  # O(log N)
            mid = (left + right) // 2  # calculate the middle index  # O(1)
            mid2 = (mid + pivot) % N  # adjust the index for rotation  # O(1)

            if nums[mid2] == target:  # check if the target is found  # O(1)
                return mid2  
            elif nums[mid2] < target:  # adjust the search range based on the comparison  # O(1)
                left = mid + 1  # move the search range to the right  # O(1)
            else:
                right = mid - 1  # move the search range to the left  # O(1)
        return -1  # return -1 if the target is not found in the rotated array  # O(1)
# Overall time complexity: O(log N)
