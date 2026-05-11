class Solution:
    def numDecodings(self, s):
        n = len(s)
        prev2 = 1  # dp[i+2]
        prev1 = 1 if s[n-1] != '0' else 0  # dp[i+1]
        
        for i in range(n-2, -1, -1):
            current = 0
            if s[i] != '0':
                current = prev1
                if int(s[i:i+2]) <= 26:
                    current += prev2
            
            prev2 = prev1
            prev1 = current
        
        return prev1