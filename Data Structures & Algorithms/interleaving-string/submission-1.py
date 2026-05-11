class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:

        if len(s1) + len(s2) != len(s3):
            return False 

        if not s1 and not s2 and not s3:
            return True 
        elif not s1 and s2 != s3:
            return False 
        elif not s2 and s1 != s3:
            return False 


        s1_processing = 'S1'
        s2_processing = 'S2'

        memo = {}

        
        def search(i, j, k):
            if i == len(s1) and j == len(s2) and k == len(s3):
                return True
            elif (i,j,k) in memo:
                return memo[(i,j,k)]
            
                
            if i < len(s1) and j < len(s2):
                if s1[i] != s3[k] and s2[j] != s3[k]:
                    memo[(i,j,k)] = False
                    return False 
                elif s1[i] == s3[k] and s2[j] == s3[k]:
                    res = search(i + 1, j, k + 1) or search(i, j + 1, k + 1)
                    memo[(i,j,k)] = res 
                    return res
                
            if i < len(s1) and s1[i] == s3[k]:
                res = search(i + 1, j, k + 1) # continuing or starting to process s1
                memo[(i,j, k)] = res
                return res 
            elif j < len(s2) and s2[j] == s3[k]:
                res = search(i, j + 1, k + 1) # continuing or starting to process s2
                memo[(i,j, k)] = res
                return res 

            memo[(i,j,k)] = False
            return False    


        return search(0, 0, 0) 

            

