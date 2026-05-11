class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        """
            h1 and h2 

            h1 > h2:
                prior to thies, we could have something 
                3, 3, 3, 1 

                at this point, we no longer can extend the 3, 3, 3 rectangle 
                so we point this off our stack and determine if its max 
                (currIdex - stack[-1][1]) * stack[-1][0]

                pop off that 3 height off stack to "stop extending" 
            
                we now use that startIndex at stack[-1][1] and start counting from the height
                of 1 
            
            h1 == h2:
                continue to extend 
                don't manipulate the stack 


            h1 < h2:
                extend both, just add to stack 

                ex) 
                    3, 6, 3
                    stack [(3,0)]
        """


        stack = [(heights[0], 0)] 
        max_area = 0 

        for i in range(1, len(heights)):
            start = i
            curr_height = heights[i] 

            # stop extending taller bars 
            while stack and stack[-1][0] > curr_height:
                height, idx = stack.pop() 
                max_area = max(max_area, (i - idx) * height)
                start = idx # carry earliest index forward 
            

            # extend current bar from earliest possible index 
            stack.append((curr_height, start))
        

        while stack:
            height, idx = stack.pop() 
            max_area = max(max_area, ((len(heights)) - idx) * height)

        return max_area



