class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0

        intervals.sort(key=lambda x: x[0]) # sort by start 

        prevEnd = intervals[0][1]
        res = 0

        for start, end in intervals[1:]: 
            if start >= prevEnd:
                prevEnd = end
            else:
                res += 1 
                prevEnd = min(end, prevEnd)

        return res