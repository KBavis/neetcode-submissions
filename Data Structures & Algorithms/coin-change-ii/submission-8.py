class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        return self.top_down(amount, coins)
        # return self.brute_force(amount, coins)

    

    def top_down(self, amount: int, coins: List[int]) -> int:

        memo = {} # only one way to form 0 amount

        def search(curr_amount, idx):
            if curr_amount == 0:
                return 1
            elif (curr_amount, idx) in memo:
                return memo[(curr_amount,idx)]
            
            total_ways = 0

            for i in range(idx, len(coins)):

                if curr_amount - coins[i] >= 0:
                    curr_amount -= coins[i]
                    total_ways += search(curr_amount, i)
                    curr_amount += coins[i]
            
            memo[(curr_amount, idx)] = total_ways 
            return memo[(curr_amount, idx)]
        

        return search(amount, 0)



    def brute_force(self, amount: int, coins: List[int]) -> int:
        
        self.total_ways = 0 

        def backtrack(curr_amount, idx):
            if curr_amount == 0:
                self.total_ways += 1 
            

            for i in range(idx, len(coins)):

                if curr_amount - coins[i] >= 0:
                    curr_amount -= coins[i]
                    backtrack(curr_amount, i)
                    curr_amount += coins[i]
        

        backtrack(amount, 0)
        return self.total_ways 