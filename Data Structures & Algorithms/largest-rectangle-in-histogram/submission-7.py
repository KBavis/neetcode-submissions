class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        if not heights:
            return 0 
        elif len(heights) == 1:
            return heights[0]


        stack = [] 
        max_area = 0

        for idx, height in enumerate(heights): 

            start_pos = idx

            # check if we can continue to extend previous heights 
            while stack and height <= stack[-1][1]:

                # 1) pop off old extension
                pos, extended_height = stack.pop() 

                # 2) determine if max area 
                curr_area = (idx - pos) * extended_height
                max_area = max(max_area, curr_area)

                # 3) update start pos for push 
                start_pos = pos 
            

            # at this point, this heigh being pushed on is the largest height on stack 
            stack.append((start_pos, height))
        

        # calculate max area (i.e ones never popped from the stack) 
        while stack:
            
            pos, extended_height = stack.pop() 
            curr = (len(heights) - pos) * extended_height
            max_area = max(max_area, curr)
        

        return max_area 






