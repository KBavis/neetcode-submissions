class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:


        i = 0 
        n = len(intervals)
        res = []

        # all prior non overlapping intervals 
        while i < n and newInterval[0] > intervals[i][1]:
            res.append(intervals[i])
            i += 1


        # at this point newInterval.start <= currInterval.end 

        # merge all overlapping intervals with newInterval 
        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval = [
                min(intervals[i][0], newInterval[0]),
                max(intervals[i][1], newInterval[1])
            ]
            i += 1 
        
        res.append(newInterval)

        while i < n:
            res.append(intervals[i])
            i += 1 
        

        return res
        