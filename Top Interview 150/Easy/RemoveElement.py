class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # pointer to not val
        k = 0
        for i in range(len(nums)):
            # swap elements
            if nums[i] != val:
                # partition
                nums[k] = nums[i]
                k += 1
        return k