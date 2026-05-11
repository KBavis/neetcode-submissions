class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        # sort the list by start date 
        sorted_intervals = sorted(intervals, key=lambda x: x[0])

        prevEnd = sorted_intervals[0][1]
        toRemove = 0 

        for currStart, currEnd in sorted_intervals[1:]:

            # overlap found ,store minimum in order to minimize conflicting overlapping intervals
            if currStart < prevEnd:  
                toRemove += 1 
                prevEnd = min(currEnd, prevEnd)
            else:
                prevEnd = currEnd 
        

        return toRemove 