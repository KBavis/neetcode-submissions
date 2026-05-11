class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        x = len(s1)
        y = len(s2)

        if x > y:
            return False 

        s1_map = [0] * 26
        s2_map = [0] * 26
        for i in range(x):
            s1_map[ord(s1[i]) - ord('a')] += 1
            s2_map[ord(s2[i]) - ord('a')] += 1

        
        for i in range(x, y):
            if s1_map == s2_map:
                return True 
            
            # move mindow forward 
            s2_map[ord(s2[i - x]) - ord('a')] -= 1
            s2_map[ord(s2[i]) - ord('a')] += 1
        
        return s1_map == s2_map
        

        
        