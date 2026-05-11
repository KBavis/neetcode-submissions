class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
            
        self.res = s[0]
        self.res_len = 1

        for i in range(len(s)):
            self.helper(i, i + 1, s)
            self.helper(i - 1, i + 1, s)
        
        return self.res

        
    def helper(self, l, r, s):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            if r - l + 1 > self.res_len:
                self.res_len = r - l + 1
                self.res = s[l:r + 1]
            
            l -= 1
            r += 1
