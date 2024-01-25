class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        # base case
        if len(nums) == 1:
            return [nums.copy()]
        # iterate through each element in the input list
        for i in range(len(nums)):
            # remove the current element from the list
            n = nums.pop(0)
            # recursively generate permutations for the remaining elements
            perms = self.permute(nums)
            # append the current element to each permutation
            for p in perms:
                p.append(n)
            # extend the result list with the generated permutations
            res.extend(perms)
            # restore the original state of the list by adding back the removed element
            nums.append(n)
        # return the final list of permutations
        return res
