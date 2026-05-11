class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        # get max # of bananas in the piles 
        max_bananas = max(piles)
        min_hourly_rate = float('inf')


        low = 1
        high = max_bananas 

        while low <= high:

            k = (low + high) // 2


            # can we eat all banana piles with rate of k in under h hours? 
            total_hours = 0
            for pile in piles:
                total_hours += math.ceil(pile / k)
            

            if total_hours <= h:
                min_hourly_rate = min(k, min_hourly_rate)
                # able to eat all bananas in allocated amount of time 
                high = k - 1
            else:
                # unable to eat all bananas, need a higher k value 
                low = k + 1 
        

        return min_hourly_rate 
