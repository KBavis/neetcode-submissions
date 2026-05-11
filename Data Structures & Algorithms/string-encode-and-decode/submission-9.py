class Solution:

    def encode(self, strs: List[str]) -> str:
        return "".join(f"{len(word)}%{word}" for word in strs)

    def decode(self, s: str) -> List[str]:

        result = [] 

        i = 0
        while i < len(s):

            # get length of word 
            j = i 
            while j < len(s) and s[j] != '%':
                j += 1
            word_len = int(s[i:j])

            j += 1 # skip percent sign 

            # extract word 
            word = s[j : j + word_len]
            result.append(word)

            # move i forward 
            i = j + word_len
        

        return result 
