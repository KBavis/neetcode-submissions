class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        # sort the position / targets based on position 
        position_and_speeds = list(zip(position, speed))
        sorted_pos_speeds = sorted(position_and_speeds, key=lambda x: x[0])
        
        stack = [] # number of hours it takes to get to destination
        for position, speed in sorted_pos_speeds:

            # solve for number of hours based on current position and speed
            curr_hours = (target - position) / speed

            # remove hours from stack that will combine with this current pos / speed
            while stack and stack[-1] <= curr_hours:
                stack.pop() 
            
            stack.append(curr_hours)
        

        return len(stack)
