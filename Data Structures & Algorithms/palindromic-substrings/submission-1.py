class Solution:
    def countSubstrings(self, s: str) -> int:
        self.pali = []

        for i in range(len(s)):
            self.helper(i, i, s)
            self.helper(i, i + 1, s)
        

        return len(self.pali)
    
    def helper(self, i, j, s):

        while i >= 0 and j < len(s) and s[i] == s[j]:
            self.pali.append(s[i:j + 1])

            j += 1
            i -= 1

        