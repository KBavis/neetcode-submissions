class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False 

        s_freq = {} 
        t_freq = {} 

        if self.get_sign(s) != self.get_sign(t):
            return False 
        else:
            return True 
        

    
    def get_sign(self, s):

        freq = [0] * 26 

        for c in s:
            freq[ord(c) - ord('a')] += 1 
        
        return freq 

