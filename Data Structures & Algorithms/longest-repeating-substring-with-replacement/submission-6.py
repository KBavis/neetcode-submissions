class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        

        freq = {} 
        maxFreq = 0 
        maxFreqChar = ''
        left = 0


        longest = 0
        for right in range(len(s)):
            
            curr = s[right]
            freq[curr] = freq.get(curr, 0) + 1 
            
            # update the maximum frequent char in current window
            if freq[curr] > maxFreq:
                maxFreq = freq[curr]
                maxFreqChar = curr
            
            # constrict when unable to replace
            window_len = (right - left) + 1 
            if window_len - maxFreq > k: 
                removed = s[left]
                freq[removed] -= 1 
                left += 1 

                # update maximum frequent if needed
                if removed == maxFreqChar:
                    maxFreq -= 1 
            

            longest = max(longest, (right - left) + 1)
        
        return longest

