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
            1. Sort start dates 
            2. Sort end dates 
            3. Find maximum ongoing meetings at once until all meetings have started
        """


        sorted_starts = sorted(interval.start for interval in intervals)
        sorted_ends = sorted(interval.end for interval in intervals)


        s = 0 
        e = 0

        res = 0
        curr = 0 
        while s < len(sorted_starts):

            # new meeting started
            if sorted_starts[s] < sorted_ends[e]:
                curr += 1 
                s += 1 
            else:
                # meeting ended 
                curr -= 1 
                e += 1 
            
            res = max(res, curr)
        

        return res 