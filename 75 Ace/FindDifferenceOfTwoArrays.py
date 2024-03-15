class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        # convert input lists to sets for efficient membership testing
        n1, n2 = set(nums1), set(nums2)
        
        # sets to store elements unique to each list
        res1, res2 = set(), set()

        # iterate through nums1 to find elements not present in nums2
        for n in nums1:
            if n not in n2:
                res1.add(n)

        # iterate through nums2 to find elements not present in nums1
        for n in nums2:
            if n not in n1:
                res2.add(n)

        # convert result sets to lists and return as a list of lists
        return [list(res1), list(res2)]
