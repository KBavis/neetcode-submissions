class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        """ 
        a) sort by position ascending 
        b) calculate total hours to get to target 
        c) remove elements from heap that have total hours <= this calculated hours
                - this essentially "merges" into lane 
                - and accounts for order 
        d) add this to our minHeap
        e) return max heap 

        """


        minHeap = [] 
        pos_and_speed = zip(position, speed)
        
        sorted_pos_and_speed = sorted(pos_and_speed, key=lambda x: x[0])

        for pos, speed in sorted_pos_and_speed:

            total_hours = self.calculateTotalHours(pos, speed, target)

            while minHeap and total_hours >= minHeap[0]:
                heapq.heappop(minHeap)
            

            heapq.heappush(minHeap, total_hours)
        
        return len(minHeap)    


    def calculateTotalHours(self, pos, speed, target):
        return (target - pos) / speed
