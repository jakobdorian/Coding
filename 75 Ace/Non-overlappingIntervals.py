class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # sort intervals based on end times.
        intervals.sort(key=lambda x: x[1])
        max_end, res = float('-inf'), 0

        # iterate through intervals.
        for start, end in intervals:
            # if current interval doesn't overlap with previous one,
            # update max_end to current end time.
            if start >= max_end:
                max_end = end
            # if current interval overlaps with previous one, increment res.
            else:
                res += 1
        # return the count of overlapping intervals.
        return res
