class Solution:
    def isPalindrome(self, s: str) -> bool:
        

        cleaned = "".join(c.lower() for c in s if c.isalnum())
        mid = len(cleaned) // 2 
        is_even = len(cleaned) % 2 == 0


        return self.is_palindrome(mid - 1, mid, cleaned) if is_even else self.is_palindrome(mid, mid, cleaned)
    

    def is_palindrome(self, l, r, s):

        while l >= 0 and r < len(s) and s[l] == s[r]:

            l -= 1 
            r += 1 
        

        return l == -1 and r == len(s)


