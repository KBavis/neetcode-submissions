class Solution:
    def isPalindrome(self, s: str) -> bool:
        

        cleaned = "".join(c.lower() for c in s if c.isalnum())

        # abcba

        mid = len(cleaned) // 2 

        return self.helper(cleaned, mid - 1, mid) if len(cleaned) % 2 == 0 else self.helper(cleaned, mid, mid)

        
    
    def helper(self, s, low, high):


        while low >= 0 and high < len(s) and s[low] == s[high]:
            low -= 1 
            high += 1 
        

        return low == -1 and high == len(s)
