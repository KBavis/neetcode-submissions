class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        """
            0. Sort intervals by start and sort queries in ascending order 
            1. Iterate through each query 
            2. Add intervals to min_heap where Interval.start <= q (only stop adding once we out of trange)
            3. While top of min heap is out of range (i.e q >= top of heap.end) we remove 
            4. Pop off top heap and add distance to output
        """



        min_heap = [] 

        sorted_intervals = sorted(intervals, key=lambda x: x[0])

        
        query_mapping = defaultdict(list) 
        for i, q in enumerate(queries):
            query_mapping[q].append(i)


        i = 0
        res = [0] * len(queries) 

        for q in sorted(query_mapping.keys()): 

            print(f"Current Query: {q}")
            
            # add new intervals that are valid given current query
            while i < len(sorted_intervals) and sorted_intervals[i][0] <= q:
                print(f"Adding the following valid interval: {sorted_intervals[i]}")
                curr_distance = sorted_intervals[i][1] - sorted_intervals[i][0] + 1
                heapq.heappush(min_heap, (curr_distance, sorted_intervals[i]))
                i += 1 
            

            # remove intervals that are no longer "in range"
            while min_heap and q > min_heap[0][1][1]:
                print(f"Remove the following interval: {min_heap[0][1]}")
                heapq.heappop(min_heap)
            

            # pop valid record (IF ANY)
            if min_heap:
                for idx in query_mapping[q]:
                    res[idx] = min_heap[0][0]
            else:
                for idx in query_mapping[q]:
                    res[idx] = -1
        
        return res 
