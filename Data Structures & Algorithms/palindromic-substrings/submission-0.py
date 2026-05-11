class Solution:
    def countSubstrings(self, s: str) -> int:
        self.palindromes = []

        for i in range(len(s)):
            self.helper(i,i,s)
            self.helper(i, i + 1, s)
        
        return len(self.palindromes)


    def helper(self, left, right, s) -> None:
        while left >= 0 and right < len(s) and s[left] == s[right]:
            self.palindromes.append(s[left: right + 1])
            left -= 1
            right += 1

        