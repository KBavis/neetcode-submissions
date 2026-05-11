class Solution:
    def trap(self, height: List[int]) -> int:
        """
            Naive Approach:
                From each height[i], expand right pointer j, while height[i] > height[j]:
                Each point, we accumulate total 

            totalAccumulated += min(maxLeft, maxRight) - height[i]

            iterate through and generate two arrays:
                maxL[i] --> maxHeight to left of this point i
                maxR[i] --> maxHeight to the right of this point i 
        
        """

        maxLeft = [float('-inf')] * len(height)
        maxRight = [float('-inf')] * len(height)

        total = 0 

        # determine max height from left
        maxHeight = height[0]
        for i in range(len(height)):
            maxHeight = max(maxHeight, height[i])
            maxLeft[i] = maxHeight 
        

        # determine max height from right 
        maxHeight = height[len(height) - 1]
        for i in range(len(height) - 1, -1, -1):
            maxHeight = max(maxHeight, height[i])
            maxRight[i] = maxHeight

        print(maxRight)
        print(maxLeft)

        # determine totals 
        for i in range(len(height)):
            total += min(maxLeft[i], maxRight[i]) - height[i]
        

        return total 