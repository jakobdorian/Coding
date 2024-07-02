class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        
        # create Counter objects to count the frequency of each element in nums1 and nums2
        c1 = Counter(nums1)
        c2 = Counter(nums2)
        
        # find the intersection of the two counters
        # the & operator returns the minimum count for each element present in both counters
        intersection = c1 & c2
        
        # iterate over each element in the intersection
        for num in intersection:
            # extend the result list with the element repeated as many times as its count in the intersection
            res.extend([num] * intersection[num])
        
        # return the result list containing the intersection of nums1 and nums2
        return res
