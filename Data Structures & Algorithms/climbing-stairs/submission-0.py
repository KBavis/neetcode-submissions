class Solution:
    def climbStairs(self, n: int) -> int:

        mapping = {0: 1, 1: 1}
        
        def fib(n):
            if n in mapping:
                return mapping[n]
            
            solution = fib(n - 1) + fib(n - 2)
            mapping[n] = solution

            return solution
        

        return fib(n)
        