class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        """
            1) Whats the most frequent character in the window? 
            2) Sliding window 
            3) Once len(current_window) - most_frequent > k, we "restart" window at right 
        """
        freq = {} 
        most_freq = 0 

        left = 0 
        right = 0 

        longest = 0

        while right < len(s): 

            curr = s[right]
            freq[curr] = freq.get(curr, 0) + 1 

            # update most frequent character 
            most_freq = max(most_freq, freq[curr])

            # check if the window needs "resetting"
            window_length = (right - left) + 1 

            if window_length - most_freq > k:
                freq[s[left]] -= 1 
                left += 1 


            longest = max(longest, right - left + 1)

            right += 1 
        

        return longest 