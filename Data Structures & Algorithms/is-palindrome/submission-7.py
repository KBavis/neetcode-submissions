class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        cleaned_str = "".join(c.lower() for c in s if c.isalnum())
        n = len(cleaned_str)

        mid = n // 2 

        return self.helper(mid, mid, cleaned_str) if n % 2 != 0 else self.helper(mid - 1, mid, cleaned_str)
    

    def helper(self, l, r, s):

        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1 
            r += 1 
        

        return l == -1 and r == len(s)


