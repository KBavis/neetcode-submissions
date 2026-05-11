class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        # count number of unique tasks 
        freq = {}
        for task in tasks:
            freq[task] = freq.get(task, 0) + 1 
        

        # construct max heap (we always want to select MAX task first)
        maxHeap = [-count for count in freq.values()] 
        heapq.heapify(maxHeap)


        time = 0 
        q = deque() # pairs of [-count, whenTaskCanExecuteAgain]

        # continue while we still have tasks to execute 
        while maxHeap or q: 

            time += 1 

            if maxHeap:
                count = 1 + heapq.heappop(maxHeap) # since maxheap, this essentially "decrements" task frequency
                if count:
                    q.append([count, time + n]) # re-add to q to indicate --> this is when we CAN process this task again 
            
            # if our queued tasks are "ready", we can re-add these to heap to be processed 
            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])
        

        return time
