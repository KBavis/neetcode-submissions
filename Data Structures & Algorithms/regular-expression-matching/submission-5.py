class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        memo = {} 

        def dfs(i, j):
            if (i,j) in memo:
                return memo[(i,j)]
            
            if i == len(s) and j == len(p):
                return True
            elif j == len(p):
                return i == len(s)
            
            does_match =  i < len(s) and (s[i] == p[j] or p[j] == '.' )

            # check if next character the start 
            if j + 1 < len(p) and p[j + 1] == '*':
                val = (
                    dfs(i, j + 2) or # 0 occurences
                    (does_match and dfs(i + 1, j)) # 1 or more occurrence 
                )

            elif does_match:

                val = dfs(i + 1, j + 1)
            else:
                val = False 
            

            memo[(i,j)] = val 
            return val 


        

        return dfs(0, 0)
