class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""

        self.longest = ""
        
        for i in range(len(s)):
            self.search(i, i, s)
            self.search(i, i + 1, s)

        return self.longest

    def search(self, i, j, s):

        while i >= 0 and j < len(s) and s[i] == s[j]:
            if (j + 1) - i > len(self.longest):
                self.longest = s[i: j + 1]
                
            i -= 1 
            j += 1


