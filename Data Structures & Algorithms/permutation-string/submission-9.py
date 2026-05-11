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
        s2_freq = self.get_frequency(s2[0: x])
        left = 0 


        for right in range(x, y):
            if s1_freq == s2_freq:
                return True 

            print(s1_freq)
            print(s2_freq)
            
            s2_freq[ord(s2[left]) - ord('a')] -= 1 
            s2_freq[ord(s2[right]) - ord('a')] += 1 

            left += 1 
        

        return s1_freq == s2_freq 
        
             


    

    def get_frequency(self, s):

        freq = [0] * 26 
        for c in s:
            freq[ord(c) - ord('a')] += 1 
        

        return freq 