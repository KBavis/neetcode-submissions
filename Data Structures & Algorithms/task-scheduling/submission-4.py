class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        """
            A - Z in tasks 

            Identical tasks must be seperated by N cpu cycles 

            May be instances where "no tasks are ready" 

            Minimum number of CPU cycles 

            When we execute a task, we need to know "when can I execute this task again"? 
                    - ex) If on iteration 2 I execute task A, and n = 2, then I can execute on iteration 5 (allows 2 complete cycles to pass)
                
            We want minimum, meaning we should greedily "execute highest number of identical tasks first" 


            maxHeap = (freqOfTask, task itself)
                    - tells us which task we should execute 

            need DS to know "when can I execute this task again"? 

            FIFO --> Queue 
                - tracks index in which we can execute this agai n
                - we peekd at queue and check (am I at this index yet?)
                - if not, we know we need to "idle" and can not execute any task currently
            

            maxHeap will first populate with the relevant frequency and task 

            we iterate while maxHeap or queue has elements (meaning further processing required)

            when we use maxHeap to select relevant task to execute, we should pop it off the stac k

            we don't re-add to heap since then we may just instantly "re-try" that task even though we know its not read 

            we should add to heap after iteration 
        """


        q = deque([])
        maxHeap = [] 

        # get frequency 
        frequency = {} 
        for task in tasks:
            frequency[task] = frequency.get(task, 0) + 1 


        # populate maxHea p
        for task in frequency:
            heapq.heappush(maxHeap, (-frequency[task], task))

        cycle_num = 1

        # determine how many intervals are required to process these tasks 
        while q or maxHeap:

            # if there elements to process in maxHeap 
            if maxHeap:

                # greedily select highest frequency task 
                neg_freq, task = heapq.heappop(maxHeap)

                # decrement total frequency (inverted since its negative)
                neg_freq += 1 

                # check if we "completed" this task, if not, re-add to queue for future processign 
                if neg_freq != 0:
                    
                    next_cycle = cycle_num + n + 1 # add additioanl one as these need to "complete"
                    q.append((next_cycle, neg_freq, task))
            

            # re-add "ready" tasks to heap
            while q and q[0][0] == cycle_num + 1:
                _, neg_freq, task = q.popleft()
                heapq.heappush(maxHeap, (neg_freq, task))

            # increment cycle num (only if additional processing required)
            if q or maxHeap:
                cycle_num += 1 
        

        return cycle_num

