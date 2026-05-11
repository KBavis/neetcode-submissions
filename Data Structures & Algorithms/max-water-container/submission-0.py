class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # maximize height of bar and maximize distance of the two bars 

        i = 0 
        j = len(heights) - 1
        max_area = 0 

        while i < j:
            
            # calculate current area 
            h1 = heights[i]
            h2 = heights[j]
            curr_area = min(h1, h2) * (j - i)
            
            # calculate max area
            max_area = max(curr_area, max_area)

            # determine which to shift 
            if h1 < h2:
                i += 1
            else: 
                j -= 1
        

        return max_area 



