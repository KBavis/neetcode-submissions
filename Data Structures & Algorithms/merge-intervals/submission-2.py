class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        
        if not intervals:
            return res
        

        intervals.sort(key=lambda x: x[0])
        res.append(intervals[0])


        for start, end in intervals[1:]:
            
            prevEnd = res[-1][1]
            if start <= prevEnd:
                res[-1][1] = max(prevEnd, end)
            else:
                res.append([start, end])
        
        return res 