class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        low = 0 
        high = len(heights) - 1 
        maxArea = 0 


        while low < high:
            
            minHeight = min(heights[low], heights[high])
            currArea = (high - low) * minHeight 

            maxArea = max(maxArea, currArea)

            if heights[low] < heights[high]:
                low += 1 
            else:
                high -= 1 
        
        return maxArea 