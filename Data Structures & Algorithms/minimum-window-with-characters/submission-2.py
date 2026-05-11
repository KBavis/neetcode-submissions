class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        freq = {} 
        for c in t:
            freq[c] = freq.get(c, 0) + 1
        
        formed = len(freq)

        j = 0
        left = 0 
        right = 0
        min_window = float('inf')

        for i in range(len(s)):

            curr = s[i]
            if curr in freq:
                freq[curr] -= 1

                if freq[curr] == 0:
                    formed -= 1
            

            while formed == 0:

                letter = s[j]
                if letter in freq:
                    freq[letter] += 1

                    if freq[letter] > 0:
                        formed += 1
                

                if i - j < min_window:
                    min_window = i - j
                    left = j
                    right = i 

                j += 1


        return s[left: right + 1] if min_window != float('inf') else ''

