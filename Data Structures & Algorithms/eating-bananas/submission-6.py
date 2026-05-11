class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """
            Goal: Determine the k, bannanas per hour. 
                - minimize k so that we can finish in time 

            Possible selections: 1 banana per hour - max(banana in piles) 


            h = 9 
            1, 2, 3, 4 

            mid_pile = 2 

            canEat = true 

            maxPile = 1, minPile = 1 
        """



        maxPile = max(piles)
        minPile = 1 

        while minPile <= maxPile:

            mid_pile = (maxPile + minPile) // 2 
            if self.canEat(piles, mid_pile, h):
                # try to minimize k if possible 
                maxPile = mid_pile - 1
            else:
                minPile = mid_pile + 1 
        

        return minPile 

    

    def canEat(self, piles, k, h):
        hours = 0 
        for pile in piles:
            hours += math.ceil(pile / k)
        
        return hours <= h
            
