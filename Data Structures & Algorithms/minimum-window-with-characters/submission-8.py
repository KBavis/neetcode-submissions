class Solution:
    def minWindow(self, s: str, t: str) -> str:
        

        freq = {}
        for c in t:
            freq[c] = freq.get(c, 0) + 1
        
        formed = len(freq)

        left, right = 0, 0 
        minLength = float('inf')

        j = 0 
        

        for i in range(len(s)):

            curr = s[i]
            if curr in freq:
                freq[curr] -= 1 
                if freq[curr] == 0:
                    formed -= 1 
            


            while formed == 0:

                if i - j < minLength:
                    right = i 
                    left = j 
                    minLength = i - j

                curr = s[j]
                if curr in freq:
                    freq[curr] += 1 
                    if freq[curr] > 0: 
                        formed += 1 
                
                j += 1 
        

        return s[left : right + 1] if minLength != float('inf') else ""