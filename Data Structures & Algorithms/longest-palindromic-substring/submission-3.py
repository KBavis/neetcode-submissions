class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        self.maxLen = 0 
        self.res = ""
        

        def search(i, j):

            while i >= 0 and j < len(s) and s[i] == s[j]:
                if j - i + 1 > self.maxLen:
                    self.maxLen = j - i + 1
                    self.res = s[i: j + 1]
                
                i -= 1
                j += 1
            
        

        for i in range(len(s)):

            search(i, i)
            search(i, i + 1)
        
        return self.res
