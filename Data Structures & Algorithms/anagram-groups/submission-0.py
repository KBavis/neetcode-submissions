class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        mapping = {}

        for i in range(len(strs)):
            signature = self.getSignature(strs[i])
            
            if signature in mapping:
                mapping[signature].append(strs[i])
            else:
                mapping[signature] = [strs[i]]
        
        result = [words for words in mapping.values()]
        return result 


    def getSignature(self, word):

        freq = [0] * 26 
        for c in word:
            freq[ord(c) - ord('a')] += 1

        return tuple(freq)
        