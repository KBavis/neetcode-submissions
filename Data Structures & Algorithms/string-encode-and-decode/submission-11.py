class Solution:

    def encode(self, strs: List[str]) -> str:
        return "".join(f"{len(s)}#{s}" for s in strs)



    def decode(self, s: str) -> List[str]:


        i = 0 
        res=  [] 
        while i < len(s):

            # extract length of string 
            j = i 
            while j < len(s) and s[j] != '#':
                j += 1 
            
            length = int(s[i: j])

            j += 1 # skip over # 

            curr = s[j: j + length]
            res.append(curr)

            i = j + length 
        

        return res 