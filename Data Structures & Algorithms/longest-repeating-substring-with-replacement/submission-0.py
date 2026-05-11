class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        freq = {} 
        max_freq = 0 
        left = 0 

        max_sub = 0

        for right in range(len(s)):
            
            curr = s[right]
            freq[curr] = freq.get(curr, 0) + 1

            max_freq = max(max_freq, freq[curr])

            window_len = right - left + 1
            if window_len - max_freq > k:
                freq[s[left]] -= 1
                left += 1
            

            max_sub = max(max_sub, right - left + 1)
        

        return max_sub 
            


