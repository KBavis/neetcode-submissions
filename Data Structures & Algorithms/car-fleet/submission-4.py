class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        vals = sorted(zip(position, speed))

        stack = [] 
        for p, s in vals:

            curr_days = (target - p) / s

            while stack and stack[-1] <= curr_days:
                stack.pop() 
            

            stack.append(curr_days)
        

        return len(stack)

            