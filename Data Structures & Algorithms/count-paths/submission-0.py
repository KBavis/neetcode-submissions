class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        visited = {}
        
        def dfs(i, j):
            if (i, j) in visited:
                return visited[(i,j)]
            elif i == m - 1 and j == n - 1:
                return 1
            elif i >= m or j >= n:
                return 0 
            
            down = dfs(i + 1, j) 
            visited[(i + 1,j)] = down
            right = dfs(i, j + 1)
            visited[(i, j + 1)] = right

            return down + right
        
        return dfs(0, 0)
