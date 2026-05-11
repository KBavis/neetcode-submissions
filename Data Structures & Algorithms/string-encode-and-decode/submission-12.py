class Solution:

    def encode(self, strs: List[str]) -> str:

        return "".join(f"{len(s)}${s}" for s in strs)


    def decode(self, s: str) -> List[str]:

        res = [] 
        i = 0 
        
        while i < len(s):

            # extract length of current word 
            j = i 
            while j < len(s) and s[j] != "$":
                j += 1 
            
            length = int(s[i:j]) 
            j += 1 # skip $ 

            res.append(s[j: j + length])

            i = j + length 
        
        return res
