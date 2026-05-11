class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        return self.getSignature(s) == self.getSignature(t)
        
    
    def getSignature(self, s: str) -> list:

        curr = [0] * 26

        for c in s:
            curr[ord(c) - ord('a')] += 1
        
        return tuple(curr)

        