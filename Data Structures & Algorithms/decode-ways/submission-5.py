class Solution:
    def numDecodings(self, s: str) -> int:
        
        memo = {len(s): 1}

        def dfs(i):
            if i in memo:
                return memo[i]
            elif s[i] == "0":
                return 0 
            

            curr = dfs(i + 1) # what's the # of ways to decode remainder of string if I take the single digit? 

            if i + 1 < len(s):
                num = int(s[i: i + 2])
                if 10 <= num <= 26:
                    curr += dfs(i + 2)
            

            memo[i] = curr 

            return memo[i]
        

        return dfs(0)
