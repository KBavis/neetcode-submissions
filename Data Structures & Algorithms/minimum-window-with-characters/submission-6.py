class Solution:
    def minWindow(self, s: str, t: str) -> str:

        freq = {} 
        min_window = float('inf')
        
        for c in t:
            freq[c] = freq.get(c, 0) + 1
        formed = len(freq)

        final_left = 0 
        final_right = 0 

        left = 0
        for right in range(len(s)): 

            curr = s[right]
            if curr in freq:
                freq[curr] -= 1

                if freq[curr] == 0:
                    formed -= 1
            
            while formed == 0: 
                if right - left + 1 < min_window:
                    final_right = right 
                    final_left = left
                    min_window = right - left + 1 
                
                curr = s[left]
                if curr in freq:
                    freq[curr] += 1
                    if freq[curr] > 0:
                        formed += 1
                
                left += 1
            
        
        return "" if min_window == float('inf') else s[final_left: final_right + 1]

                

            
        