class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals or len(intervals) == 1:
            return intervals

        sorted_intervals = sorted(intervals, key=lambda x: x[0])
        res = [sorted_intervals[0]]

        for curr_start, curr_end in sorted_intervals[1:]:
            

            prev_start = res[-1][0] if res else float('-inf')
            prev_end = res[-1][1] if res else float('-inf')

            # can merge!
            if curr_start <= prev_end:
                res[-1] = [
                    min(prev_start, curr_start),
                    max(prev_end, curr_end)
                ]
            else:
                res.append([
                    curr_start, 
                    curr_end
                ])
        

        return res 