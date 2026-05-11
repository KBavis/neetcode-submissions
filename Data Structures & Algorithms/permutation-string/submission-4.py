class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        x = len(s1)
        y = len(s2)
        
        s1_sign = self._get_sign(s1)
        s2_sign = self._get_sign(s2[:x])


        for i in range(x, y):
            if s1_sign == s2_sign:
                return True 
            
            s2_sign[ord(s2[i - x]) - ord('a')] -= 1
            s2_sign[ord(s2[i]) - ord('a')] += 1 
        

        return s1_sign == s2_sign
        

    
    def _get_sign(self, s):

        freq = [0] * 26 
        
        for c in s:
            freq[ord(c) - ord('a')] += 1 
        
        return freq 