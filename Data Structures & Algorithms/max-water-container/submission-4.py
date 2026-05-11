class Solution:
    def maxArea(self, heights: List[int]) -> int:

        # 7 - 1 = 6 
        
        max_area = 0 

        l, r = 0, len(heights) - 1

        while l < r:

            h1 = heights[l]
            h2 = heights[r]
            width = r - l 

            max_area = max(max_area, width * min(h1, h2))

            if h1 < h2:
                l += 1 
            else:
                r -= 1 
        

        return max_area 