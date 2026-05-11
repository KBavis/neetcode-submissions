class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        

        # sort intervals by start date 
        intervals.sort(key=lambda x: x[0])

        prevEnd = intervals[0][1]
        res = 0
        for currStart, currEnd in intervals[1:]:

            if currStart < prevEnd:
                res += 1 
                prevEnd = min(prevEnd, currEnd)
            else:
                prevEnd = currEnd 
        

        return res 
