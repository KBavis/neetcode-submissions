class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        
        intervals.sort(key=lambda x: x[0])
        result = [intervals[0]]

        for start, end in intervals[1:]:

            prev_end = result[-1][1]

            # check if mergable 
            if start <= prev_end:
                result[-1][1] = max(prev_end, end)
            else:
                result.append([start, end])
            

        return result