class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        seen = set()
        longest_sub = 0 
        
        left = 0 
        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1 
            
            seen.add(s[right])
            longest_sub = max(longest_sub, len(seen))
        

        return longest_sub 
