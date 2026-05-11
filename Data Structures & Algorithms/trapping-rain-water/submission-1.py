class Solution:
    def trap(self, height: List[int]) -> int:
        
        res = [0] * len(height)

        # calculate left max 
        leftMax = 0
        for i in range(len(height)):
            res[i] = leftMax 
            leftMax = max(leftMax, height[i])
        
        # calculate right max & min 
        rightMax = 0
        for i in range(len(height) - 1, -1, -1):
            res[i] = min(rightMax, res[i])
            rightMax = max(rightMax, height[i])
        

        total = 0 
        for i in range(len(height)):
            total += max(0, res[i] - height[i])
        
        return total
