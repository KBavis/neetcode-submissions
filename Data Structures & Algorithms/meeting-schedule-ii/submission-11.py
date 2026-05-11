"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        
        if not intervals:
            return 0 
        elif len(intervals) == 1:
            return 1 
        

        starts = sorted(interval.start for interval in intervals)
        ends = sorted(interval.end for interval in intervals)

        s = 0 
        e = 0 
        curr = 0
        res = 0

        while s < len(starts):

            if starts[s] < ends[e]:
                s += 1 
                curr += 1 
            else:
                e += 1 
                curr -= 1 
            
            res = max(curr, res)
        
        return res 