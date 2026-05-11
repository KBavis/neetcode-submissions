class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    

        def get_signature(curr: str):
            signature = [0] * 26 

            for c in curr: 
                signature[ord(c) - ord('a')] += 1
            
            return tuple(signature) 

        mapping = {}
        for curr in strs:
            curr_sign = get_signature(curr)
            if curr_sign in mapping:
                mapping[curr_sign].append(curr)
            else:
                mapping[curr_sign] = [curr]
        
        
        return [vals for vals in mapping.values()]

        


        