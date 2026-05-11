class Solution:

    def encode(self, strs: List[str]) -> str:
        return "".join(f"{len(s)}%{s}" for s in strs)

    def decode(self, s: str) -> List[str]:
        i = 0 
        result = []

        while i < len(s):
            j = i
            
            while s[j] != "%":
                j += 1
            num = s[i:j]
            length = int(num)

            j += 1
            
            result.append(s[j:j + length])

            i = j + length
        
        return result

            

