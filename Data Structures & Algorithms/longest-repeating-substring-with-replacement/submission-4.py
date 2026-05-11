class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        freq = {} 
        maxFreq = 0 
        max_len = 0

        left = 0 
        for right in range(len(s)):
            curr = s[right]
            freq[curr] = freq.get(curr, 0) + 1 
            maxFreq = max(maxFreq, freq[curr])

            window_len = (right - left) + 1
            if window_len - maxFreq > k:
                freq[s[left]] -= 1
                left += 1
            
            max_len = max(right - left + 1, max_len)
        
        return max_len