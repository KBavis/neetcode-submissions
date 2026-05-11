class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        intervals.append(newInterval)
        intervals.sort(key=lambda x: x[0])
        results = [intervals[0]]

        # find overlap and merge 
        for start, end in intervals[1:]:

            prevEnd = results[-1][1]
            if start <= prevEnd:
                results[-1][1] = max(end, prevEnd)
            else:
                results.append([start,end])
        
        return results 