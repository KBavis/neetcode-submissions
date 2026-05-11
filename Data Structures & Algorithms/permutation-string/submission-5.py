class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        x = len(s1)
        y = len(s2)
        
        if x > y:
            return False 
        


        s1_freq = self.get_sign(s1)
        s2_freq = self.get_sign(s2[:x])

        for i in range(x, y):
            if s1_freq == s2_freq:
                return True 
            
            s2_freq[ord(s2[i - x]) - ord('a')] -= 1 
            s2_freq[ord(s2[i]) - ord('a')] += 1 
        
        return s1_freq == s2_freq 
    

    def get_sign(self, s):

        freq = [0] * 26 

        for c in s:
            freq[ord(c) - ord('a')] += 1 
        

        return freq 