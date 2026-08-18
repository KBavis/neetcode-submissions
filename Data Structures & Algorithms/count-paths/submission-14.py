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


        dp = [[0] * (n + 1) for _ in range(m + 1)]
        dp[m - 1][n - 1] = 1
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                dp[i][j] += dp[i + 1][j] + dp[i][j + 1]
        
        print(dp)
        return dp[0][0]