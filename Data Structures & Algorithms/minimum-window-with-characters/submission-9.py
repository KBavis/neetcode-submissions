class Solution:
    def minWindow(self, s: str, t: str) -> str:

        frequency = {}
        for c in t:
            frequency[c] = frequency.get(c, 0) + 1 

        formed = len(frequency)

        min_window = float('inf')
        l = 0 
        r = 0

        left = 0 
        right = 0 

        while right < len(s):

            curr = s[right]
            if curr in frequency:
                frequency[curr] -= 1 
                if frequency[curr] == 0:
                    formed -= 1
            

            # constrict when we find valid substring 
            while formed == 0:

                if right - left + 1 < min_window:
                    min_window = right - left + 1 
                    l = left
                    r = right 

                curr = s[left] 
                if curr in frequency:
                    frequency[curr] += 1 
                    if frequency[curr] > 0:
                        formed += 1 
                
                left += 1 
            

            # move right pointer forward
            right += 1 


        return "" if min_window == float('inf') else s[l: r + 1]
