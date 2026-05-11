class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False 
        
        s_chars = [0] * 26 
        t_chars = [0] * 26 

        i, j = 0, 0 
        while i < len(s) or j < len(t):

            if i < len(s):
                c = s[i]
                s_chars[ord(c) - ord('a')] += 1
                i += 1
            
            if j < len(t):
                c = t[j]
                t_chars[ord(c) - ord('a')] += 1
                j += 1
            
        
        return s_chars == t_chars 
