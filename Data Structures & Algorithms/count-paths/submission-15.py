class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        """
            Brute Force Solution:
                --> try to go through and calculate every single unique route from 
                --> almost like a back tracking problem from every sqaure 
                    --> always attemptign to go left, right, down, up and jsut skipping if we've been there before 
            

            More Efficient Solution:
                start from the ending point and leverage the fact that we're always going to just have two spots we can potentially go
                this being down or up 
        """

        # return self.bottomUp(m, n)
        self.memo = {}
        self.m = m
        self.n = n
        return self.topDown(0, 0)
    
    def topDown(self, i, j):
        if (i,j) in self.memo:
            return self.memo[(i,j)]
        elif i == self.m - 1 and j == self.n - 1:
            return 1 
        elif i >= self.m or j >= self.n:
            return 0
    
        total = self.topDown(i + 1, j) + self.topDown(i, j + 1)
        self.memo[(i,j)] = total 

        return total 





    def bottomUp(self, m, n):
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        dp[m - 1][n - 1] = 1
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                dp[i][j] += dp[i + 1][j] + dp[i][j + 1]
        
        print(dp)
        return dp[0][0]