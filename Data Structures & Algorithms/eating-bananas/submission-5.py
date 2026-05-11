class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        

        # range 1 --> max # of bannanas in a pile 

        max_bananas = max(piles)
        n = len(piles)

        low = 1 
        high = max_bananas 

        while low <= high:

            k = (low + high) // 2 

            # can we eat n piles in k hours ? if so, minimize. if not, increase k
            if self.can_finish(piles, k, h):
                high = k - 1 
            else:
                low = k + 1 
        
        return low 
    

    def can_finish(self, piles, k, max_hours):

        hours = 0
        for pile in piles:
            hours += math.ceil(pile / k)
        
        return hours <= max_hours
            





