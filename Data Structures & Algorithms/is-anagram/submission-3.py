class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if not s and not t:
            return True 
        elif not s or not t or len(s) != len(t):
            return False 

        return self.get_sign(s) == self.get_sign(t)

    
    def get_sign(self, s):
        freq = [0] * 26 

        for c in s:
            freq[ord(c) - ord('a')] += 1 
        
        return freq