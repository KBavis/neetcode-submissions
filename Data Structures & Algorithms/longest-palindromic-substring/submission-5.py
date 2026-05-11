class Solution:
    def longestPalindrome(self, s: str) -> str:

        self.max_length = 0
        self.l = 0 
        self.r = 0 

        for i in range(len(s)):

            # check the odd and even substrings 
            self.helper(i, i, s)
            self.helper(i - 1, i, s)

        

        return s[self.l : self.r + 1] if self.max_length != 0 else "" 

        
    

    def helper(self, left, right, s):
        if not s:
            return

        while left >= 0 and right < len(s) and s[left] == s[right]:
            # check if we exceeded the max length 
            if (right - left) + 1 >= self.max_length:
                self.max_length = (right - left) + 1
                self.l = left 
                self.r = right 

            left -= 1 
            right += 1 
