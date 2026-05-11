class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        freq = {}
        left = 0 
        max_char = float('-inf')
        max_len = 0

        for right in range(len(s)):
            c = s[right]
            freq[c] = freq.get(c, 0) + 1
            
            max_char = max(max_char, freq[c])
            window_len = right - left + 1

            if window_len - max_char > k:
                freq[s[left]] -= 1
                left += 1
            
            max_len = max(max_len, right - left + 1)
        
        return max_len
