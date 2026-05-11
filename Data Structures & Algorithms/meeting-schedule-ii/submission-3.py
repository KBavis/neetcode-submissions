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
        
        start_times = sorted(x.start for x in intervals)
        end_times = sorted(x.end for x in intervals)

        s, e = 0, 0 
        res = 0
        count = 0

        while s < len(intervals):
            
            if start_times[s] < end_times[e]:
                count += 1
                s += 1 
            else:
                count -= 1 
                e += 1 
            
            res = max(res, count)
        
        return res 