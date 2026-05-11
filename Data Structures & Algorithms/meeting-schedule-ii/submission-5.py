"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        
        """
            1. Sort by start date --> O(nlogn) operation
            2. Find overlap --> [a1, a2], [b1, b2] --> a1 < b2 and b1 < a2 
            3. In order minimize the the number of days we need to take the smaller of the two ends going forward when checking overlap
        """

        # base case 
        if len(intervals) <= 1:
            return len(intervals)

        start_times = sorted(interval.start for interval in intervals)
        end_times = sorted(interval.end for interval in intervals)

        s, e = 0, 0 
        res = 0 
        curr_meetings = 0

        while s < len(intervals):

            if start_times[s] < end_times[e]:
                curr_meetings += 1 
                s += 1
            else:
                curr_meetings -= 1 
                e += 1 
            
            res = max(curr_meetings, res)
        
        return res 

        