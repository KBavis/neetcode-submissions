"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if not intervals:
            return True

        intervals.sort(key=lambda x: x.start)
        maxEnd = intervals[0].end


        for interval in intervals[1:]:

            start = interval.start
            end = interval.end

            if start < maxEnd:
                return False 
            else:
                maxEnd = max(maxEnd, end) 
        

        return True 
