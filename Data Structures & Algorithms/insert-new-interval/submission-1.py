class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        results = []
        i = 0 
        n = len(intervals)

        # add all intervals prior to new interval start
        while i < n and intervals[i][1] < newInterval[0]:
            results.append(intervals[i])
            i += 1
        
        # merge all overlapping intervals with new interval 
        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval = [
                min(newInterval[0], intervals[i][0]),
                max(newInterval[1], intervals[i][1])
            ]
            i += 1 

        results.append(newInterval)

        # add remaining intervals 
        while i < n:
            results.append(intervals[i])
            i += 1


        return results