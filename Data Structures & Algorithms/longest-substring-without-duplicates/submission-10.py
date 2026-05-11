class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        seen = set() 
        res = 0

        left = 0
        for right in range(len(s)):
            while seen and s[right] in seen:
                seen.remove(s[left])
                left += 1 
            
            seen.add(s[right])
            res = max(res, len(seen))
        

        return res 

