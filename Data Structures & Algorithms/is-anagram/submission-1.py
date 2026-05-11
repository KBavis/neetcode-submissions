class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        return self.getSignature(s) == self.getSignature(t)
        
    
    def getSignature(self, s: str) -> list:

        freq = {}

        for c in s:
            freq[c] = freq.get(c, 0) + 1
        
        return freq

        