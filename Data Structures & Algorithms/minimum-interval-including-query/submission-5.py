class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        """
            Core Idea: 
                We need to find the smallest interval in intervlas where a query can belong 
                Naive approach would be to iterate through each query and then iterate through intervals each tiem      
                    EX) query 2 --> check each interval and determine which it can belong in and is smallest 
        """

        # create mapping of query back to original index 
        query_mapping = defaultdict(list)
        for i, q in enumerate(queries):
            query_mapping[q].append(i)

        # sort intervals based on start date 
        sorted_intervals = sorted(intervals, key=lambda x: x[0])
        sorted_queries = sorted(queries)

        print(f"Query Mapping={query_mapping}")
        print(f"Sorted Intervals = {sorted_intervals}, Sorted Queries = {sorted_queries}")

        res = [0] * len(queries)

        min_heap = [] 
        idx = 0 # index to store current location in sorted intervals 
        for curr_query in sorted_queries: 

            # dynamically append intervals while in range 
            while idx < len(sorted_intervals) and curr_query >= sorted_intervals[idx][0]:
                distance = (sorted_intervals[idx][1] - sorted_intervals[idx][0]) + 1
                print(f"Pushing Interval={sorted_intervals[idx]} onto MinHeap with Distance = {distance}")
                heapq.heappush(min_heap, (distance, sorted_intervals[idx]))
                idx += 1
            

            # remove intervals that are out of range (end-dated in pas)
            while min_heap and min_heap[0][1][1] < curr_query:
                heapq.heappop(min_heap) 

            if min_heap:
                print(f"Interval={min_heap[0]}, Query={curr_query}")
            else:
                print(f"Interval=-1, Query={curr_query}")
            
            # update res 
            if min_heap:
                idxs = query_mapping[curr_query]
                for i in idxs:
                    res[i] = min_heap[0][0]
            else:
                idxs = query_mapping[curr_query]
                for i in idxs:
                    res[i] = -1
        

        return res 


        