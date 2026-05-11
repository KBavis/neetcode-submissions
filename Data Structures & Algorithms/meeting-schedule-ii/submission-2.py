"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        
        start_times = sorted(i.start for i in intervals)
        end_times = sorted(i.end for i in intervals)

        s, e = 0, 0
        res, count = 0, 0


        while s < len(intervals):

            if start_times[s] < end_times[e]:
                count += 1 
                s += 1 
            else:
                count -= 1 
                e += 1 
            
            res = max(res, count)
        
        return res
        