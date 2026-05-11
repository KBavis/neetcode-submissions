class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        """
            Naive Solution: O(n^2), take current day, iterate through remaining 
        """

        if not temperatures:
            return []

        stack = [] 
        res = [0] * len(temperatures)

        for i, temp in enumerate(temperatures):

            # remove from stack & add to result while top of stack < curr temp 
            while stack and stack[-1][0] < temp:
                val = stack.pop()
                res[val[1]] = i - val[1]
            
            # add new element to stack 
            stack.append((temp, i))
        

        # account for temperatures on stack with no higher next temperatures 
        while stack:
            val = stack.pop()
            res[val[1]] = 0
        
        return res 