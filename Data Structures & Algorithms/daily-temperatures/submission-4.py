class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        res = [0] * len(temperatures)

        stack = [] 

        for i, curr in enumerate(temperatures):
            
            while stack and stack[-1][0] < curr:
                temp, idx = stack.pop() 
                res[idx] = i - idx
            
            stack.append((curr, i))
        

        # add to res for those with not higher temperatures 
        while stack:
            temp, idx, = stack.pop() 
            res[idx] = 0
        
        return res 