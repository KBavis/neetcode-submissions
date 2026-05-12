class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        """
            - Positions & Speeds & Target 
            - Position = [1], Speeds = [4] --> car is at position 1, traveling at a speed of 4 mph 


            If another car, is driving slower than a car behind it, the car behind it "merges" to join a fleet

            Limited by the car in front of it 

            Alwasy restricted by the car in HIGHER POSITION having a HIGHER TIME 

            1. Zip the postion and speeds together 
            2. Sort these by their position (in ascending order)
                --> car at postion 3, t = 40 
                --> car at position 6, t = 50 
            3. Calculate the total time this car will take to get there 
            4. Remove entires from our minHeap where minHeap[0] <= currTime 
        """


        stack = [] 

        # zip our position and targets 
        speed_and_pos = zip(speed, position)

        # sort by position in ascending order 
        sorted_speed_and_pos = sorted(speed_and_pos, key=lambda x: x[1])
        


        for i in range(len(sorted_speed_and_pos)):

            speed, pos = sorted_speed_and_pos[i]

            # calculate total hours to completion 
            total_hours = self.calculate_hours(target, speed, pos)

            # remove prior entries that are <= hours (restricted by these hours)
            while stack and stack[-1] <= total_hours:
                stack.pop() 
            
            stack.append(total_hours)
        

        return len(stack)
    

    def calculate_hours(self, target, speed, pos):
        return (target - pos) / speed