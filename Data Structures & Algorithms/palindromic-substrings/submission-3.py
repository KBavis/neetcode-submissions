class Solution:
    def countSubstrings(self, s: str) -> int:
        

        total = 0 
        for i in range(len(s)):
            
            total += self.helper(i - 1, i, s)
            total += self.helper(i, i, s)
        
        return total 


    

    def helper(self, left, right, s):
        if not s:
            return 0 
        
        ways = 0 

        while left >= 0 and right < len(s) and s[left] == s[right]:
            ways += 1 
            left -= 1 
            right += 1 
        
        return ways 