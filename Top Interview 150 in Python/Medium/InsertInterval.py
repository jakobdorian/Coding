class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        # iterate through list of intervals
        for i in range(len(intervals)):
            # new interval is smaller than the start value
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:]
            # new interval is larger than the start value
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i])
            # new interval is overlapping the current interval, if so merge
            else:
                newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]
        
        res.append(newInterval)
        return res
