class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        
        """
            combination of s1 and s2 == s3 

            x = len(s1)
            y = len(s2)

            x + y == len(s3) OR we fail 

            DIVIDE s1 and s2 into substring 
                m = # of s1 substrings
                n = # of s2 substrings 
            

            | m - n | <= 1 

            previously character

            Input: s1 = "aaaa", s2 = "bbbb", s3 = "aabbbbaa"

            Input: s1 = "aa", s2 = "a" , s3 = "a"

            What happens when they're the same ?
                i --> pointer for s1 
                j --> pointer for s2 

                if s1[i] == s2[j], which do we take? 
                    --> try both paths:
                        res = recurse(i + 1, j) or recurse(i, j + 1)

                memo[(i,j)]
        """

        # store previously determined states 
        memo = {}

        # handle sceanrio where (s1 + s2) > (s3) or (s1 + s2) < (s3)
        if len(s1) + len(s2) != len(s3):
            return False 



        def dfs(i: int, j: int) -> bool:
            """
                i --> pointer for s1 
                j --> pointer for s2 
            """
            
            if i == len(s1) and j == len(s2):
                return True 
            elif (i,j) in memo:
                return memo[(i,j)]
            

            # either i or j could be >= respective string 
            s1_char = s1[i] if i < len(s1) else None 
            s2_char = s2[j] if j < len(s2) else None 
            s3_char = s3[i + j] 

            # check if they are both equal 
            if s1_char == s3_char and s2_char == s3_char:
                # check both paths 
                res = (dfs(i + 1, j) or dfs(i, j + 1))
            elif s1_char == s3_char:
                # increment s1 path
                res = dfs(i + 1, j)
            elif s2_char == s3_char:
                # increment s2 path 
                res = dfs(i, j + 1)
            else:
                # neither of the current characters match s3 
                res = False 
            

            # memoize the current state 
            memo[(i,j)] = res 
            return res 
        

        return dfs(0, 0)
