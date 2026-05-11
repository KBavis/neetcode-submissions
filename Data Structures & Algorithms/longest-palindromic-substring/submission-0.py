class Solution:
    def longestPalindrome(self, s: str) -> str:
        self.res = ""
        self.resLen = 0 

        for i in range(len(s)):
            # odd length 
            self.search(i, i, s)
            
            # even length 
            self.search(i, i + 1, s)

        return self.res

    def search(self, l, r, s):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            if (r - l + 1) > self.resLen:
                self.res = s[l: r + 1]
                self.resLen = r - l + 1
                
            l -= 1
            r +=1
        

            
