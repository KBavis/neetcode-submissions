class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        """
            Determine count of each task

            Attempt to address task with highest counts first 

            Need to have some sort of mechanism to determine highest priority task
                - Heap? 
            

            Need mechanism to track when we can tackle particular task 
        """


        maxHeap = [] 
        count = {} 

        # count tasks
        for task in tasks:
            count[task] = count.get(task, 0) + 1 
        

        # get max heap to determine "highest priority" task to complete 
        for task, total in count.items():
            heapq.heappush(maxHeap, (-total, task))
        

        # queue to track "when can I execute task again"
        q = deque([])
        time = 1 

        while maxHeap or q:

            # process task if possible 
            if maxHeap:
                total_count, task = heapq.heappop(maxHeap)
                print(f"Processing Task: {task}, Count={count}")
                total_count += 1 

                # no need to add to queue, as the task is complete
                if total_count != 0:
                    q.append((time + n, total_count, task))
            
            # determine if we can add task back to maxHeap to be processed
            if q:
                # task is ready to be processed next iteration
                if q[0][0] == time:
                    _, total_count, task = q.popleft() 
                    print(f"Task={task}, is ready to be processed next loop!")
                    heapq.heappush(maxHeap, (total_count, task))

            
            if maxHeap or q:
                time += 1 # only increment if nothing left to process 

        return time 
                    
