class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        maxArea = 0 
        stack = [] # pair --> (index, height)


        for i, curr_height in enumerate(heights):

            start = i 
            while stack and stack[-1][1] > curr_height: 
                index, height = stack.pop() 
                maxArea = max(maxArea, height * (i - index))
                start = index # since we already noted that curr_height <  height, we know that curr_height can extend backward to this idx
            
            # add start index that we push all the way backwards
            stack.append((start, curr_height))

        
        # we may still have heights on stack (i.e if heights in increasing order)
        for i, h in stack:
            maxArea = max(maxArea, h * (len(heights) - i)) # since it was never popped from stack, 
            # we know that the height made it all the way to end!
        
        return maxArea