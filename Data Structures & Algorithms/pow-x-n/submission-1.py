class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 0:
            return 0 
        
        if n == 0:
            return 1 

        total = 1
        for i in range(abs(n)):
            total *= x
        
        return total if n > 0 else 1 / total