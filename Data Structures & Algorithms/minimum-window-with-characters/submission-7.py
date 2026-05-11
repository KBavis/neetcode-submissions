class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""
        
        x = len(s)
        y = len(t)

        if x < y:
            return ""
        

        freq = {} 
        for c in t:
            freq[c] = freq.get(c, 0) + 1
        formed = len(freq)

        final_left = 0
        final_right = 0 
        min_window = float('inf')

        left = 0
        for right in range(len(s)):

            curr = s[right]
            if curr in freq:
                freq[curr] -= 1 

                if freq[curr] == 0:
                    formed -= 1 
            

            while formed == 0:

                if right - left < min_window:
                    min_window = right - left 
                    final_right = right 
                    final_left = left 

                curr = s[left]
                if curr in freq:
                    freq[curr] += 1 

                    if freq[curr] > 0:
                        formed += 1 

                left += 1 
        

        return s[final_left : final_right + 1] if min_window != float('inf') else ""
            
            

