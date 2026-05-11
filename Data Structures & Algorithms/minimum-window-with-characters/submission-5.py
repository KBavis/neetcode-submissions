class Solution:
    def minWindow(self, s: str, t: str) -> str:

        freq = {}
        for c in t:
            freq[c] = freq.get(c, 0) + 1
        
        formed = len(freq)

        left = 0 
        right = 0 
        final_left = 0
        final_right = 0 

        min_window = float('inf')


        while right < len(s):

            curr = s[right]
            if curr in freq:
                freq[curr] -= 1

                if freq[curr] == 0: 
                    formed -= 1
            

            while formed == 0: 

                if right - left < min_window:
                    final_left = left 
                    final_right = right 
                    min_window = right - left 
                
                curr = s[left]
                if curr in freq:
                    freq[curr] += 1

                    if freq[curr] > 0: 
                        formed += 1
                
                left += 1
            
            right += 1
        

        return s[final_left: final_right + 1] if min_window != float('inf') else "" 
                
            




        