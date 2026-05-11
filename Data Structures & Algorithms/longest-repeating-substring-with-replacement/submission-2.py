class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        # within window, calculate the maximum frequency 

        # left, right pointers 

        # need to mvoe? window length - max frequency > k --> shift 

        # max length = max(right - left + 1, max length)

        left = 0 
        freq = {} 
        max_freq = 0
        longest = 0

        for right in range(len(s)):
            
            curr = s[right]
            freq[curr] = freq.get(curr, 0) + 1

            max_freq = max(max_freq, freq[curr])

            window_len = right - left + 1
            if window_len - max_freq > k:
                freq[s[left]] -= 1
                left += 1
            

            longest = max(right - left + 1, longest)
        
        return longest 