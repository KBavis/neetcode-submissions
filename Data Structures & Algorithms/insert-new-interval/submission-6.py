class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        res = [] 

        # insert the inital intervals that have no intersection 
        i = 0
        while i < len(intervals) and newInterval[0] > intervals[i][1]:
            res.append(intervals[i])
            i += 1 

        # merge intervals 
        while i < len(intervals) and intervals[i][0] <= newInterval[1]:
            newInterval = [
                min(intervals[i][0], newInterval[0]), 
                max(intervals[i][1], newInterval[1])
            ]
            i += 1 
        res.append(newInterval)

        # add remaining intervals if any 
        while i < len(intervals):
            res.append(intervals[i])
            i += 1 


        return res 
        

