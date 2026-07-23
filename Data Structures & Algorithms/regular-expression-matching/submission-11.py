class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        """
            DP sort of problem with two sepreate pointers 

            We need to levarege a pointer for s (i) and a pointer for p (j) to transverse down each of the lists 

            If we ever get to a pointer where i == len(s) and p == len(j), when we can return True 
                - all we need is a single match in order to indicate that these two are going to be matched 
            
            Need to handle fact that one of the pointers (i) can reach the end of its 
            string but the other one (j) may not, this dones't necessarily imply that its a failure 
            since we have to account for *'s

            Handling .
                - as long as the other pointer != len(string) then we're good
            

            Handling * 
                - always need to check if the character following the current character is going to contain the * 
                - if it does, then we have to account for two paths 
                    a) skipping the current character (just increment pointer for this one BY TWO, and not the other one)
                    b) repeating the current chracter (don't increment pointer for this one, but increment next one)
                        --> How do we handle infinity loop? 
                            --> for example, in example 2, we keep increment i until its == 3
                            --> however, this should be covered when we try scenario a) 
            

            Memoization will be by 2D (i,j is unique state)
        """
        
        memo = {} 

        def dfs(i, j):
            if i == len(s) and j == len(p):
                return True 
            elif (i,j) in memo:
                return memo[(i,j)]
            elif j == len(p):
                # if we ever reach the end of the pattern, this is invalid
                return False 
            
            res = False 

            # step 1: determine if the next character is * 
            if j + 1 < len(p) and p[j + 1] == "*":

                # step 1a) attempt to just skip chracter altogether 
                res = dfs(i, j + 2)

                # step 1b) attempt to repeat character (only a valid route in the case that the current characters match)
                if not res and i < len(s) and (s[i] == p[j] or p[j] == "."): # only check if skip route failed
                    res = dfs(i + 1, j)

            # step 2: determine if the current character is .
            elif p[j] == ".":
                res = dfs(i + 1, j + 1)
            # step 3: determine the two character match
            else:
                res = False 
                if i < len(s) and s[i] == p[j]:
                    res = dfs(i + 1, j + 1)
            

            # memoize result 
            memo[(i,j)] = res 
            return res 
        

        return dfs(0, 0)

            








