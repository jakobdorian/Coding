class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        # edge cases
        if not points:
            return 0
        # sort array
        points.sort()
        prev_balloon = points[0]
        # number of arrows, min would be 1
        res = 1
        # iterate list starting from second item
        for start, end in points[1:]:
            # check if the current ballon is bigger than the next
            if start > prev_balloon[1]:
                res += 1
                prev_balloon = [start, end]
            # check if it is smaller
            else:
                prev_balloon[1] = min(prev_balloon[1], end)
        return res
