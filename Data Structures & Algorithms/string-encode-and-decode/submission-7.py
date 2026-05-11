class Solution:

    def encode(self, strs: List[str]) -> str:

        return "".join(f"{len(word)}#{word}" for word in strs)


    def decode(self, s: str) -> List[str]:
        i = 0
        result = []

        while i < len(s):

            j = i 

            while s[j] != '#':
                j += 1
            

            length = int(s[i:j])

            j += 1 # skip # 

            result.append(s[j:j+length])

            i = j + length 
        
        return result



