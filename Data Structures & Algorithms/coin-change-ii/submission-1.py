class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        memo = {}
        return self.backtrack(0, amount, coins, memo)
    
    def backtrack(self, idx, target, coins, memo):
        if target == 0:
            return 1 
        elif (idx, target) in memo:
            return memo[(idx, target)]

        
        total = 0 
        for i in range(idx, len(coins)):
            if target - coins[i] >= 0:
                target -= coins[i]
                
                total += self.backtrack(i, target, coins, memo)

                target += coins[i]
        

        memo[(idx, target)] = total 
        return total
