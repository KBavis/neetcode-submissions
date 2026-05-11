"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if not intervals or len(intervals) == 1:
            return True 

        sorted_intervals = sorted(intervals, key=lambda x: x.start)
        prev_end = sorted_intervals[0].end

        """
            [x1, x2], [y1, y2]

            y1 < x2 and x1 < y2
        """

        prev_end = sorted_intervals[0].end

        for interval in sorted_intervals[1:]: 

            if interval.start < prev_end:
                return False 
            else:
                prev_end = interval.end
        
        return True 

                
