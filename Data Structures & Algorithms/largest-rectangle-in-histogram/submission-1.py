class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        stack = [] # (index, height)
        maxArea = 0


        for i, curr_height in enumerate(heights):

            start = i 
            while stack and stack[-1][1] > curr_height:

                idx, height = stack.pop() 
                maxArea = max(maxArea, height * (i - idx))
                start = idx # since  currHeight < prevHeight, we can extend backward to this index 
            

            stack.append((start, curr_height))
        


        for i, h in stack:
            maxArea = max(maxArea, h * (len(heights) - i))
        

        return maxArea