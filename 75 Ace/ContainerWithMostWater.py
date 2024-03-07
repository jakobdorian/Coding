# O(n) solution
class Solution:
    def maxArea(self, height: List[int]) -> int:
        res = 0
        p1 = 0
        p2 = len(height) - 1
        
        # iterate until left pointer is less than right pointer
        while p1 < p2:
            # compute the area between the two pointers
            area =  (p2 - p1) * min(height[p1], height[p2])
            # update the maximum area encountered so far
            res = max(res, area)
            
            # move the pointer that corresponds to the smaller height
            if height[p1] < height[p2]:
                p1 += 1
            else:
                p2 -= 1
        
        # return the maximum area
        return res