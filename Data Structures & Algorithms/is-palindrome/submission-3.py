class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        parsed = "".join(c.lower() for c in s if c.isalnum())

        left = 0
        right = len(parsed) - 1 

        print(parsed)

        while left <= right:
            if parsed[left] != parsed[right]:
                return False 
            
            left += 1
            right -= 1
        
        return True 