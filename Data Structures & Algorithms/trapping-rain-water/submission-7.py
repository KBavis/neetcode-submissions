class Solution:
    def trap(self, height: List[int]) -> int:
        
        """ 
            O(n^2)
                i = 0, move j forward while currHeight <= height[0] OR j reaches len(height)
                j = "searc


            Intution:
                leverage 2 pointers to solve the problem 

                left pointer = 0, right pointer = len(heights) - 1 

                always limited by the smaller height, so move that pointer "inward" 

                height[len(height) - 1] = 1 
                height[len(height) - 2] = 2 
                currRightMax = 2 

                IF height at len(height) - 1 was 2 and the height at len(height) - 2 was 1, 
                we could hold 1 drop of water 

                1) Keep track of left max and right max 
                2) determine which pointer to shift inward
                3) calculate the new right/left max 
                4) calculate water holding by doing currMax - height[pointer] and adding that to tal 
        """

        l = 0 
        r = len(height) - 1 

        res = 0 
        currLeftMax = height[l]
        currRightMax = height[r]

        while l < r:

            currLeft = height[l]
            currRight = height[r]

            # shift left pointer inward
            if currLeft < currRight:
                l += 1 
                currLeftMax = max(currLeftMax, height[l])
                res += currLeftMax - height[l]
            else:
                r -= 1 
                currRightMax = max(currRightMax, height[r])
                res += currRightMax - height[r]
        

        return res 

            