# O(n) sol
class Solution:
    def maxArea(self, height: List[int]) -> int:
        res = 0
        # for p1 range(len(height)):
        #     for p2 in range(l + 1, len(height)):
        #         # compute area
        #         area =  (p2 - p1) * min(height[p1], height[p2])
        #         # max area, update res
        #         res = max(res, area)
        # return res 
        p1 = 0
        p2 = len(height) - 1
        
        # while left is less than right
        while p1 < p2:
            # compute area
            area =  (p2 - p1) * min(height[p1], height[p2])
            # max area, update res
            res = max(res, area)
            if height[p1] < height[p2]:
                p1 += 1
            else:
                p2 -= 1
        return res
        