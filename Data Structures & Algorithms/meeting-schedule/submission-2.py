"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:

        #(a1, a2), (b1, b2)

        # overlap --> if b1 < a2 AND a1 < b2 --> (3, 6), (4, 8)
        if not intervals or len(intervals) == 1:
            return True 

        intervals.sort(key=lambda x: x.start)

        prevEnd = intervals[0].end
        for curr in intervals[1:]: 
            if curr.start < prevEnd:
                return False 
            
            prevEnd = curr.end 
        
        return True 
