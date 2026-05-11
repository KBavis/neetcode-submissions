class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        """
        Note: This represents our K-range 

        The idea is that we will always take a min of 1 banana per hour, up to the maximum number of bananas in all piles
        """
        l, r = 1, max(piles) 

        res = r

        while l <= r:
            
            # 
            k = (l + r) // 2

            # accumulate total number of hours to eat each pile
            hours = 0 
            for p in piles: 
                hours += math.ceil(p / k) # NOTE: If it takes 1.2 hours, we round up to 2 hours 
            
            # valid k rate found, attempt to minimize
            if hours <= h:
                res = min(res, k)

                r = k - 1 # search left portion to minimize 
            else:
                l = k + 1 # rate was too small, search right portion 
        

        return res 