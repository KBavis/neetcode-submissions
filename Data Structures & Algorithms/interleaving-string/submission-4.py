class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        
        """ 

        i --> s1 pointer
        j --> s2 pointer
        k --> s3 pointer 

        if i == len(s1) and j == len(s2) and k == len(s3):
            return True 
        elif k == len(s3):
            return False 


        if both i and j == k ? 
            return dfs(i + 1, j, k + 1) or dfs(i, j + 1, k + 1) 
        """

        memo = {}

        def dfs(i, j, k): 
            if i == len(s1) and j == len(s2) and k == len(s3):
                return True 
            elif k == len(s3):
                return False 
            elif (i,j,k) in memo:
                return memo[(i,j,k)]
            
            # check if equal 
            s1_char = s1[i] if i < len(s1) else ""
            s2_char = s2[j] if j < len(s2) else ""
            s3_char = s3[k] 

            if s1_char == s3_char and s2_char == s3_char:
                ret = dfs(i + 1, j, k + 1) or dfs(i, j + 1, k + 1)
            elif s1_char == s3_char:
                ret = dfs(i + 1, j, k + 1)
            elif s2_char == s3_char:
                ret = dfs(i, j + 1, k + 1)
            else:
                ret = False 
            

            memo[(i,j,k)] = ret
            return ret
        

        return dfs(0, 0, 0)
