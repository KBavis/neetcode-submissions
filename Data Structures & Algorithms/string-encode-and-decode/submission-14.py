class Solution:

    def encode(self, strs: List[str]) -> str:
        # 4:loop66:<jjjjjjjj....>

        return "".join(f"{len(s)}:{s}" for s in strs)

    def decode(self, s: str) -> List[str]:

        i = 0 
        res = []

        while i < len(s):

            j = i 
            while j < len(s) and s[j] != ":":
                j += 1 
            
            length = int(s[i:j])

            j += 1 # skip delimeter


            res.append(s[j: j + length])

            i = j + length 
        
        return res