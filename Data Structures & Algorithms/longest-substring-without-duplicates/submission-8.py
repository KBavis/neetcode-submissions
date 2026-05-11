class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        l = 0
        seen = set() 
        max_len = 0

        for c in s:
            while c in seen:
                seen.remove(s[l])
                l += 1
            
            seen.add(c)
            max_len = max(max_len, len(seen))
        

        return max_len 
            