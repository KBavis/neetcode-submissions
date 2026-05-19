class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        if not s1 and not s2:
            return True 
        elif not s2 or not s2 or len(s1) > len(s2):
            return False 
        
        x = len(s1)
        y = len(s2)

        s1_freq = self.get_freq(s1)
        s2_freq = self.get_freq(s2[:x])

        # i = 3

        for i in range(x, y):
            if s1_freq == s2_freq:
                return True 
            
            # update s2 freq 
            old_char = s2[i - x]
            new_char = s2[i]

            s2_freq[ord(old_char) - ord('a')] -= 1
            s2_freq[ord(new_char) - ord('a')] += 1 
        

        return s1_freq == s2_freq


    def get_freq(self, s):

        freq = [0] * 26
        for c in s:
            freq[ord(c) - ord('a')] += 1 
        
        return freq 