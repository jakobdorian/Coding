class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # hashset to keep all values in our window
        window = set()
        l = 0
        # go through each value
        for r in range(len(nums)):
            # check if the window is too large
            if r - l > k:
                window.remove(nums[l])
                l += 1
            # check if the current value is a dulplicate
            if nums[r] in window:
                return True
            # if not add it to our window set
            window.add(nums[r])
        return False
