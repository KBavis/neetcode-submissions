class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        cleaned_str = "".join(c.lower() for c in s if c.isalnum())

        # odd --> aba --> start both pointers at len(s) // 2 
        # even --> abbaa --> start left pointer at len(s) // 2 - 1, len(s) // 2 
        mid = len(cleaned_str) // 2

        return self.helper(cleaned_str, mid, mid) if len(cleaned_str) % 2 != 0 else self.helper(cleaned_str, mid - 1, mid)

    
    def helper(self, s, left, right):

        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1 
            right += 1 
        

        return right == len(s) and left == -1
