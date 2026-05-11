class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        cars = sorted(zip(position, speed))
        
        stack = [] 
        for curr_pos, curr_speed in cars:

            # calculate total iterations to get to target based on current positon and speed
            iterations = (target - curr_pos) / curr_speed 

            # remove all previous values from stack that are < current iterations 
            while stack and stack[-1] <= iterations:
                stack.pop() 
            
            # add new # of iteratiosn 
            stack.append(iterations)
        

        return len(stack)
