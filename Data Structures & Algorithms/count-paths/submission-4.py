class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        

        memo = [[-1 for j in range(n)] for i in range(m)]

        def dfs(i, j):

            if i == m - 1 and j == n - 1:
                return 1
            elif i >= m or j >= n:
                return 0
            elif memo[i][j] != - 1:
                return memo[i][j]
            
            curr = dfs(i + 1, j) + dfs(i, j + 1)
            memo[i][j] = curr 

            return curr 
        

        return dfs(0,0)
            



