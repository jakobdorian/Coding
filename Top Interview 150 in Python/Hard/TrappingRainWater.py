class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        # empty input
        if not height:
            return 0
        # left and right pointer
        l = 0
        r = len(height) - 1
        # max heights for each pointer
        lmax = height[l]
        rmax = height[r]

        while l < r:
            if lmax < rmax:
                l += 1
                lmax = max(lmax, height[l])
                # never should be negative
                res += lmax - height[l]
            else:
                r -= 1
                rmax = max(rmax, height[r])
                res += rmax - height[r]
        return res
        