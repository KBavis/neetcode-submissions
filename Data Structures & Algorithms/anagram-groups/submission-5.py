class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        

        mapping = {} 

        for s in strs:
            frequency = self.get_freq(s)

            if frequency in mapping:
                mapping[frequency].append(s)
            else:
                mapping[frequency] = [s]
        

        # generate solution 
        return [v for v in mapping.values()]
    

    def get_freq(self, s):

        freq = [0] * 26 
        for c in s:
            freq[ord(c) - ord('a')] += 1 
        

        return tuple(freq)