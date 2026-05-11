class Solution:

    def encode(self, strs: List[str]) -> str:

        # 2$aa4$bbbb

        return "".join(f"{len(s)}${s}" for s in strs)

    def decode(self, s: str) -> List[str]:

        i = 0 
        n = len(s)
        res = [] 

        while i < n:

            # extract length of current word 
            j = i 
            while j < n and s[j] != "$":
                j += 1 
            word_len = int(s[i: j])

            j += 1 # skip the dollar sign 

            # extract word 
            word = s[j: j + word_len]

            # append to result 
            res.append(word)

            # move i forward 
            i = j + word_len 
        

        return res 

