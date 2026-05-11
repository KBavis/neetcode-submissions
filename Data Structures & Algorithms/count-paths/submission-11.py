class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        

        dp = [[0] * (n + 1) for _ in range(m + 1)]
        dp[m - 1][n - 1] = 1 


        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if j == n - 1 and i == m - 1:
                    print('Here!')
                    continue

                print(f"Adding {dp[i+1][j]} + {dp[i][j + 1]}")
                dp[i][j] = dp[i + 1][j] + dp[i][j + 1]
            
            print(f"State of DP: {dp}")
        

        return dp[0][0]
        

