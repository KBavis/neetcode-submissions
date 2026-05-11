class Solution:
    def countSubstrings(self, s: str) -> int:
        
        total_count = 0 

        for i in range(len(s)):
            total_count += self.helper(s, i, i + 1)
            total_count += self.helper(s, i, i)
        
        return total_count

    
    def helper(self, s, low, high):

        curr_count = 0 

        while low >= 0 and high < len(s) and s[low] == s[high]:
            curr_count += 1 

            low -= 1 
            high += 1 
        
        return curr_count
    

    # iterate through n times 

    # 