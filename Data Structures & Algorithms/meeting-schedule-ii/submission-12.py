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
            Find the minimum number of days required to seperate meetings 

            Overlap ==> [a1, a2], [b1, b2] ==> a1 < b2 and b1 < a2 

            Sort by start date 

            0, 40 
            5, 10 
            15, 20 

            Whats the maximum number of meetings that we have going on at one time 

            [0, 5, 15]
            [10, 20, 40]

            s = 0 
            e = 0 

            maxConcurrent = 1 
            curr = 1 

            new start date ? curr += 1 
        """

        start_dates = sorted([i.start for i in intervals])
        end_dates = sorted([i.end for i in intervals])

        s = 0
        e = 0 
        maxConcurrent = 0
        curr = 0 

        while s < len(intervals):

            # check if we can start another meeting 
            if start_dates[s] < end_dates[e]:
                curr += 1 
                maxConcurrent = max(maxConcurrent, curr)
                s += 1 
            else:
                curr -= 1 
                e += 1 
        
        return maxConcurrent 
        