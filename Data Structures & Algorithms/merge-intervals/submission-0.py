class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        # sort 
        sorted_intervals = sorted(intervals, key=lambda x: x[0])
        output = [sorted_intervals[0]]

        # merge 
        for start, end in sorted_intervals[1:]:
            prev_end = output[-1][1]

            if start <= prev_end:
                output[-1][1] = max(prev_end, end)
            else:
                output.append([start,end])
    
        return output