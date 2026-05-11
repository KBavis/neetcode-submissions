class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        return self.get_freq(s) == self.get_freq(t)
        
    
    def get_freq(self, s):

        freq = {} 
        for c in s:
            freq[c] = freq.get(c, 0) + 1 
        
        return freq