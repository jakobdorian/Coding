class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        res = 0
        # count of odd numbers encountered so far
        odd = 0
        
        # two pointers to manage the sliding window
        left, mid = 0, 0

        # iterate through the array with the right pointer
        for right in range(len(nums)):
            # if the current number is odd, increment the odd counter
            if nums[right] % 2:
                odd += 1
            
            # if the count of odd numbers exceeds k, move the left pointer to reduce the count
            while odd > k:
                # if the number at the left pointer is odd, decrement the odd counter
                if nums[left] % 2:
                    odd -= 1
                # move the left pointer to the right
                left += 1
                # update mid to the current position of the left pointer
                mid = left

            # when the number of odd numbers equals k, count the valid subarrays
            if odd == k:
                # move the mid pointer to the right while the numbers are even
                while not nums[mid] % 2:
                    mid += 1
                # calculate the number of subarrays ending at the current right pointer
                # and starting at each position from left to mid (inclusive)
                res += (mid - left) + 1
        
        # return the total number of valid subarrays
        return res
