class Solution:
    def numDecodings(self, s: str) -> int:
        

        """
            If dealing with a single number, there's only one decode this 
            

            If dealing with multiple numbers, 
                we only account for the "second" way (L) if the total is between 
                0 <= x <= 26

            2060

            dfs(i):

                total_ways += dfs(i + 1)

                can I take two characters?
                    i.e 0 <= int(s[i: i + 2]) <= 26 

                    if so, total_ways += dfs(i + 2)
        """


        memo = {len(s): 1}

        def dfs(i):
            if i in memo:
                return memo[i]
            elif s[i] == '0':
                return 0
            

            # determine total # of ways from taking a single number
            total_ways = dfs(i + 1)

            # check if we decode using both strings 
            if i + 2 <= len(s):
                
                # if numeric is between 0 - 26, we can decode 
                value = int(s[i: i + 2])
                if 0 <= value <= 26:
                    total_ways += dfs(i + 2)

            memo[i] = total_ways 
            return total_ways 
        

        return dfs(0)
