class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        max_freq = 0
        freq = {} 
        left = 0
        max_len = 0

        for right in range(len(s)):
            c = s[right]

            freq[c] = freq.get(c, 0) + 1
            max_freq = max(max_freq, freq[c])

            window_len = right - left + 1

            if window_len - max_freq > k:
                freq[s[left]] -= 1
                left += 1
            
            
            max_len = max(max_len, right - left + 1)
        
        return max_len


