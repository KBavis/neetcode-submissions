class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        mapping = {} 

        for s in strs:
            freq = self.get_freq(s)

            if freq in mapping:
                mapping[freq].append(s)
            else:
                mapping[freq] = [s]
        
        res = [vals for vals in mapping.values()]
        return res

    
    def get_freq(self, s):

        freq = [0] * 26 

        for c in s:
            freq[ord(c) - ord('a')] += 1 
        
        return tuple(freq)  