class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        """ 

        Naive:
            find instance where s[i] == t[0] 

            once found, search for subseuqnece 

            O(n^2)
        
        Recursvie 

            Case 1: s[i] != t[j], where is currnet index, and j is the current index in 2 
                - increment i, leave j alone 
            

            Case 2: s[i] == t[j]:
                - increment i, increment j 
                - increment i, leave j as is 
            

            Base Case:
                j == len(t):
                    return 1 
                
                i == len(s):
                    return 0 
                

                total_ways = dfs(i + 1, j + 1)
                total_ways += dfs(i + 1, j)
        """

        memo = {(len(s), len(t)): 1}


        def dfs(i, j):
            if (i, j) in memo:
                return memo[(i,j)]
            elif i == len(s):
                return 0 
            elif j == len(t):
                return 1
            
            if s[i] != t[j]:
                total_ways = dfs(i + 1, j)
                memo[(i,j)] = total_ways
                return total_ways
            else:
                total_ways = dfs(i + 1, j)
                total_ways += dfs(i + 1, j + 1)
                memo[(i,j)] = total_ways 
                return total_ways 
        

        return dfs(0, 0)
