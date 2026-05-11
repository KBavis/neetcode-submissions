"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:

        # (a, b) --> (c, d) OVERLAP = if c < b and a < d 
        if not intervals:
            return True

        intervals.sort(key=lambda x: x.start) 

        prevEnd = intervals[0].end 

        for interval in intervals[1:]:

            if interval.start < prevEnd:
                return False 
            
            prevEnd = interval.end

        return True 

