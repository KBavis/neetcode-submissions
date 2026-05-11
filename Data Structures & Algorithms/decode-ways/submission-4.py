class Solution:
    def numDecodings(self, s: str) -> int:

        # 2 choices --> 1) # of ways to decode using single numeric, 2) # of ways to decode using two numerics 

        memo = {len(s): 1}
        def dfs(i):
            if i in memo:
                return memo[i]
            elif s[i] == "0":
                return 0
            
            curr = dfs(i + 1)
            if i + 1 < len(s):
                digits = int(s[i: i + 2])
                if 10 <= digits <= 26:
                    curr += dfs(i + 2)
            
            memo[i] = curr
            return curr 
        

        return dfs(0)
        