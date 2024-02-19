class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # Initialize an array to store lengths of longest increasing subsequences
        res = [1] * len(nums)  # O(n)

        # Iterate through the nums list in reverse order
        # Complexity: O(n^2)
        for i in range(len(nums) - 1, -1, -1):
            for j in range(i + 1, len(nums)):
                # Check if the current number is less than the number ahead
                if nums[i] < nums[j]:
                    # Update the length of longest increasing subsequence if applicable
                    res[i] = max(res[i], 1 + res[j])

        # Return the maximum value in the result array
        # Complexity: O(n)
        return max(res)

# Overall Time Complexity: O(n^2)
# Overall Space Complexity: O(n)
