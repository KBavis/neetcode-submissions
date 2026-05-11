class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        return self.get_frequency(s) == self.get_frequency(t)
        
    
    def get_frequency(self, s):

        if not s:
            return []
        

        freq = [0] * 26 
        for c in s:
            freq[ord(c) - ord('a')] += 1 

        return freq