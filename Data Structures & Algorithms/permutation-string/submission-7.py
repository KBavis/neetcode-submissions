class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        freq_to_check = self.get_frequency(s1)
        
        x = len(s1)
        y = len(s2)

        left = 0
        for right in range(x, y):
            if freq_to_check == self.get_frequency(s2[left: right]):
                return True 
            
            left += 1 
        
        return freq_to_check == self.get_frequency(s2[y - x: y])
    

    def get_frequency(self, s):

        freq = [0] * 26 
        for c in s:
            freq[ord(c) - ord('a')] += 1 
        

        return freq