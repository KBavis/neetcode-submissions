class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        """     
        Overlap --> 

            [x1, x2], [y1, y2]

            y1 < x2 && x1 < y2 

            sort by start, then x1 < y2 is given, we just need to check that 
            y1 < x2 


            [1, 7], [3, 5], [5, 6]
        """
        if not intervals or len(intervals) <= 1:
            return 0

        sorted_intervals = sorted(intervals, key=lambda x: x[0])

        prev_end = sorted_intervals[0][1]
        total = 0

        print(sorted_intervals)

        for curr_start, curr_end in sorted_intervals[1:]:

            if curr_start < prev_end: 
                total += 1 
                prev_end = min(curr_end, prev_end)
            else:
                prev_end = curr_end 
        
        return total
