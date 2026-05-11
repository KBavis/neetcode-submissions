class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        

        seen = set()
        left = 0
        longest = 0

        for c in s:
            while c in seen:
                seen.remove(s[left])
                left += 1 
            
            seen.add(c)
            longest = max(longest, len(seen))
        
        return longest 
