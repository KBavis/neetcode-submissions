class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        """
        Brute Force: 
            - try to go through and execute whatever task is next 
            - put it on hold and execute the next task that is available 
            - continue doing this until we have completed every task 
            - try a different variation next time 
        
        Optimized Greedy Approach:
            - iterate through and get a count of each task 
            - always choose to go through and select the task with LARGEST remaining tasks left 
            - once we've selected this task, we should enque this task and add the designated "time" point when we can execute next


        O(n) time for constructing dictionary, O(k) space

        O(klogk) for constructing the initial heap 

        O(nlogk)
        """


        # get count of total tasks
        grouped_tasks = defaultdict(int)
        for task in tasks: 
            grouped_tasks[task] += 1 
        
        # queue for storing next time we can execute a task 
        queue = deque([])

        # max_heap for determining which task is next to execute 
        max_heap = []
        for task, count in grouped_tasks.items():
            heapq.heappush(max_heap, (-count, task))
        

        # must continue iterating while there are tasks 
        # in queue to be executed OR tasks we can currently
        # process waiting to be executed 
        num_cycles = 0

        while max_heap or queue:

            # NOTE: FAST FORWARD IN THIS CASE MAKES THIS O(NlogK), INSTEAD OF O(num_cycles + NlogK)
            if not max_heap and not queue:
                num_cycles = queue[0][2]

            # determine if there are items on the queue now ready for processing 
            while queue and num_cycles > queue[0][2]:

                # NOTE: we will skip adding tasks to the queue in the case that there are NO remaining tasks
                # so all tasks on the queue have a remaining count 
                task, remaining_count, ready_cycle = queue.popleft()
                heapq.heappush(max_heap, (remaining_count, task))
            

            # determine task with largest remaining tasks to process IF there are tasks in the ready state
            if max_heap:
                negative_count, task = heapq.heappop(max_heap)
                
                # new count is negative count + 1 since its a max heap 
                new_count = negative_count + 1 

                # only enque if the new count < 0 
                if new_count < 0:
                    queue.append((task, new_count, num_cycles + n))



            num_cycles += 1 
        

        return num_cycles 


"""
    num_cycles = 0 
    max_heap = [(-2, X), (-2, Y)]
    queue = []

    num_cycles = 1 
    max_heap = [(-2, Y)]
    queue = [(X, -1, 2)]

    num_cycles = 2 
    max_heap = [] 
    queue = [(X, -1, 2), (Y, -1, 3)]

    num_cycles = 3 
"""

