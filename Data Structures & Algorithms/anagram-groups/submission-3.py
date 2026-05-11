class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        


        mapping = {}
        for s in strs:
            signature = self.get_sign(s)

            if signature in mapping:
                mapping[signature].append(s)
            else:
                mapping[signature] = [s] 
        

        return [curr for curr in mapping.values() ]

    
    def get_sign(self, s):

        freq = [0] * 26

        for c in s:
            freq[ord(c) - ord('a')] += 1

        return tuple(freq) 