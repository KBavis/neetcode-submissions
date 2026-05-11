class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if not s1 and not s2:
            return True 
        elif not s1 or not s2:
            return False 
        elif len(s1) > len(s2):
            return False 
        
        x = len(s1)
        y = len(s2)

        s1_freq = self.get_frequency(s1)
        left = 0 


        for right in range(x, y):
            if s1_freq == self.get_frequency(s2[left: right]):
                return True 
            
            left += 1 
        

        return s1_freq == self.get_frequency(s2[left: y])
        
             


    

    def get_frequency(self, s):

        freq = [0] * 26 
        for c in s:
            freq[ord(c) - ord('a')] += 1 
        

        return freq 