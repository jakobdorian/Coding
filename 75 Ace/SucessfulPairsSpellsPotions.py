class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        res = [] 
        for s in spells:  
            left, right = 0, len(potions) - 1  # set up pointers for binary search
            temp = len(potions)  # temporary variable to store the index of the potion

            # binary search for the number of successful pairs
            while left <= right:
                mid = (left + right) // 2  # calculate the middle index
                # If the product of spell and potion value is greater than or equal to success
                if s * potions[mid] >= success:
                    right = mid - 1  # update the right pointer
                    temp = mid  # update the temporary variable to store the current index
                else:
                    left = mid + 1  # update the left pointer
            res.append(len(potions) - temp)  # append the count of successful pairs to the result list
        return res
