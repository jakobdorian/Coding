class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []
        
        def helper(build, num, summ):
            if len(build) == k:
                if summ == n:
                    res.append(build)
            # iterate from the current number up to 9
            for i in range(num, 9+1):
                if summ + i > n: # if adding i exceeds the target sum n, exit loop
                    break
                helper(build + [i],i+1, summ + i)
        
        helper([],1,0)
        # return the list of combinations
        return res
                
