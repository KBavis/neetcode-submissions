class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        min_window = float('inf')
        left = 0
        right = 0 
        i = 0
        j = 0

        freq = {} 
        for c in t:
            freq[c] = freq.get(c, 0) + 1
        formed = len(freq)

        while j < len(s):

            curr = s[j]
            if curr in freq:
                freq[curr] -= 1
                if freq[curr] == 0:
                    formed -= 1
            

            # minimize window 
            while formed == 0: 
                
                if j - i < min_window:
                    min_window = j - i
                    left = i 
                    right = j 
                

                c = s[i]
                if c in freq:
                    freq[c] += 1
                    if freq[c] > 0:
                        formed += 1

                i += 1
            

            j += 1

        return s[left:right + 1] if min_window != float('inf') else ""