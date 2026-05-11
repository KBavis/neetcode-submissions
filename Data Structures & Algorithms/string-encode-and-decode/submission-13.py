class Solution:

    def encode(self, strs: List[str]) -> str:
        # len(word):<word>
        return "".join(f"{len(s)}:{s}" for s in strs)

    def decode(self, s: str) -> List[str]:

        # 5:Hello5:World

        res = [] 
        i = 0 

        while i < len(s):
            
            # extract length of current word
            j = i 
            while j < len(s) and s[j] != ":":
                j += 1 
            curr_len = int(s[i:j])

            j+= 1 # skip over the delimter ':' 
            
            curr_word = s[j: j + curr_len]
            res.append(curr_word)

            i = j + curr_len
        
        return res 

            

