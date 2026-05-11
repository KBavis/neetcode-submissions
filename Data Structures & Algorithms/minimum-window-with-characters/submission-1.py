class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        left = 0
        right = 0
        i = 0 
        j = 0 
        min_window = float('inf')

        if len(t) > len(s):
            return ""

        
        freq = {}
        for c in t:
            freq[c] = freq.get(c, 0) + 1
        
        found = len(freq)

        while i < len(s):

            curr = s[i]

            if curr in freq:
                freq[curr] -= 1
                if freq[curr] == 0:
                    found -= 1
            
            while found == 0:

                if i - j < min_window:
                    min_window = i - j
                    left = j
                    right = i 


                # constrict window 
                c = s[j]
                if c in freq:
                    freq[c] += 1
                    if freq[c] > 0:
                        found += 1
                
                j += 1
            
            i += 1
        
        if min_window == float('inf'):
            return ""

        return s[left:right + 1]
