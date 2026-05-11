class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        if not heights:
            return 0 
        

        i , j = 0, len(heights) - 1
        maxHeight = 0

        while i < j:

            h1 = heights[i] 
            h2 = heights[j]

            base = j - i 
            height = min(h1, h2)

            maxHeight = max(maxHeight, base * height)

            if h1 < h2:
                i += 1
            else:
                j -= 1 
        
        return maxHeight