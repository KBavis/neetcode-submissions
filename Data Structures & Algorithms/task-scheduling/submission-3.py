class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        """
            1. Get a frequenecy of the same tasks --> {X: 2, Y: 2}
            2. Greedy --> always choose task with largest number of tasks remaining 
            3. Keep a queue of tasks that are not "ready" to be executed
                    - Which task is "pending" 
                    - When a task is "ready" to be removed from queue and added back to heap for processing 

            a) Queue for "tasks pending n cycles since last execution" 
            b) Heap for storing "highest priority task" to complete 
                    - Use a max heap in order to greedily choose task with largest number of tasks remaining 
        """

        # get frequency of tasks O(n)
        task_frequency = {}
        for task in tasks:
            task_frequency[task] = task_frequency.get(task, 0) + 1 
        

        # consturct max heap 
        values = [-val for val in task_frequency.values()]
        heapq.heapify(values) 
        max_heap = values

        # setup queue 
        q = deque([])

        curr_time = 0 

        while q or max_heap: 
            curr_time += 1 

            # execute current task & re-append to queue for later processing if needed
            if max_heap:
                tasks_remaining = 1 + heapq.heappop(max_heap)
                if tasks_remaining != 0:
                    q.append((curr_time + n, tasks_remaining))

            # check if task idle period is over, if so, re-add to heap 
            if q and q[0][0] == curr_time: 
                _, tasks_remaining = q.popleft() 
                heapq.heappush(max_heap, tasks_remaining)
        
        return curr_time 

            
            
    


