class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        # maximum number of points on a line
        res = 1
        # loop through each point in the list
        for i in range(len(points)):
            # the first point
            p1 = points[i]
            # dictionary to store the count of slopes
            count = collections.defaultdict(int)
            
            # iterate through the remaining points
            for j in range(i + 1, len(points)):
                # the second point
                p2 = points[j]
                # calculate the slope between the two points
                if p2[0] == p1[0]:
                    # if the x-coordinates are equal, set the slope to infinity
                    slope = float("inf")
                else:
                    # calculate the slope using the formula (y2 - y1) / (x2 - x1)
                    slope = (p2[1] - p1[1]) / (p2[0] - p1[0])
                
                # increment the count of the current slope in the dictionary
                count[slope] += 1
                
                # update the maximum number of points on a line
                res = max(res, count[slope] + 1)
        
        # return the maximum number of points on a line
        return res
