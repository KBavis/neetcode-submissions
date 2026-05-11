class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        max_length = 0
        for i in range(len(s)):
            seen = set()
            j = i
            
            while j < len(s) and s[j] not in seen:
                seen.add(s[j])
                j += 1
            
            max_length = max(max_length, j - i)
            i = j



        # if not s:
        #     return 0

        # i = 0 
        # j = 1 
        # max_substring = 1

        # while i < len(s):
        #     seen = set() 
        #     j = i 

        #     while j < len(s) and s[j] not in seen:
        #         seen.add(s[j])
        #         j += 1
            

        #     max_substring = max(j - i, max_substring)

        #     i = j
        
        return max_length
            
        