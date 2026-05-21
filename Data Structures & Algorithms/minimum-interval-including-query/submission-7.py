class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        
        return self.efficient_solution(intervals, queries)

        
    def efficient_solution(self, intervals, queries): 
        """
            Instead of having this be O(n * m) solution, how could we make this better? 

            1) Sort intervals by start date 
            2) Sort queries by their start date 
                    - create mapping of query to corresponding location (account for multiple queries that are same)
            
            3) Iterate through queries in order 
                    - add intervals that have start <= current query to minHeap (retain end date info)
                    - incremetn pointer of i to reflect where we are in intervals query 
                    - after all intervals added, remove intervals where end date < query 
                    - one at the top is the one we add 
        """

        # sort intervals
        sorted_intervals = sorted(intervals, key=lambda x: x[0])
        
        # preserve original location of queries 
        queries_to_idx = defaultdict(list)
        for i, query in enumerate(queries):
            queries_to_idx[query].append(i)
        
        # sort queries 
        sorted_queries = sorted(queries)

        min_heap = [] # (length, start, end)
        i = 0

        res = [-1] * len(queries)

        for q in sorted_queries:

            # add intervals that have start <= q
            while i < len(sorted_intervals) and sorted_intervals[i][0] <= q:
                
                start = sorted_intervals[i][0]
                end = sorted_intervals[i][1]

                heapq.heappush(
                    min_heap,
                    ((end - start) + 1,
                    start, 
                    end)
                )
                i += 1 
            

            # remove intervals that are terminated early 
            while min_heap and min_heap[0][2] < q:
                heapq.heappop(min_heap)
            

            # if there is a remaining interval, this is the smallest one 
            if min_heap:

                distance = min_heap[0][0]
                for idx in queries_to_idx[q]:
                    res[idx] = distance 
        
        return res 



    def brute_force(self, intervals, queries):
        
        lengths = [(end - start) + 1 for start, end in intervals]
        interval_and_size = list(zip(intervals, lengths))

        res = []

        for query in queries:

            min_length = float('inf')
            for interval, length in interval_and_size:
                print(f"Interval: {interval}, Query: {query}, Length={length}")
                if self.in_interval(interval[0], interval[1], query):
                    min_length = min(min_length, length)

            smallest_interval = min_length if min_length != float('inf') else -1 
            print(f"Smallest Interval for Query={query} : {smallest_interval}")
            res.append(smallest_interval)
        
        return res
        


    def in_interval(self, start, end, x):
        print(f"Checking if {x} >= {start} and {x} <= {end}")
        return x >= start and x <= end 