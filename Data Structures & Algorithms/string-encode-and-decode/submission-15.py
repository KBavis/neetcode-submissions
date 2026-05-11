class Solution:

    def encode(self, strs: List[str]) -> str:
        # format --> <length>:<string> 
        return "".join(f"{len(s)}:{s}" for s in strs)

    def decode(self, s: str) -> List[str]:
        
        res = [] 
        i = 0
        while i < len(s):

            # extract length of current string 
            j = i 
            while j < len(s) and s[j] != ":":
                j += 1 
            length = int(s[i:j])
            j += 1

            # extract current word 
            curr_word = s[j: j + length]

            # append to res 
            res.append(curr_word)

            # shift pointer forward 
            i = j + length 
        
        return res 

