class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        # edge case
        if not nums:
            return []
        # intialize pointers
        start, cur = nums[0], nums[0]
        end = None
        res = []
        # iterate from second number in array
        for n in nums[1:]:
            cur += 1
            if n == cur:
                end = n
            else:
                if not end:
                    res.append(str(start))
                else:
                    res.append(str(start)+"->"+str(end))
                start = n
                cur = n
                end = None
        
        if not end:
            res.append(str(start))
        else:
            res.append(str(start)+"->"+str(end))
        return res
