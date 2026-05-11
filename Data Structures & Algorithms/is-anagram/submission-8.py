class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        return self.get_freq(s) == self.get_freq(t)
        
    

    def get_freq(self, s):

        freq = [0] * 26
        for c in s:
            freq[ord(c) - ord('a')] += 1 
        

        return freq