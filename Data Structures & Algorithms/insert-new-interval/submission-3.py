class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        i = 0 
        n = len(intervals)

        res = []

        while i < n and newInterval[0] > intervals[i][1]:
            res.append(intervals[i])
            i += 1 
        

        # the above loop has validated that by this point intervals[i].endDate <= newInterval.startDate
        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval = [
                min(newInterval[0], intervals[i][0]),
                max(newInterval[1], intervals[i][1])
            ]
            i += 1 
        
        res.append(newInterval)

        # finish remaining non-overlapping intervals 
        while i < n:
            res.append(intervals[i])
            i += 1 
        

        return res
