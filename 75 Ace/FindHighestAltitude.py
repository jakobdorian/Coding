class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        # variables to keep track of current altitude and maximum altitude encountered
        curr, res = 0, 0

        # iterate through each gain value
        for i in gain:
            # update current altitude by adding the gain
            curr += i
            # update maximum altitude encountered so far
            res = max(curr, res)
        
        # return the maximum altitude encountered
        return res
