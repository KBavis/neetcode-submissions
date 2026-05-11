class Solution:
    def isPalindrome(self, s: str) -> bool:
        

        cleaned = "".join(c.lower() for c in s if c.isalnum())

        mid = len(cleaned) // 2

        return self.helper(mid - 1, mid, cleaned) if len(cleaned) % 2 == 0 else self.helper(mid, mid, cleaned)
    

    def helper(self, start, end, s):

        while start >= 0 and end < len(s) and s[start] == s[end]:

            start -= 1
            end += 1 
        

        return start == -1 and end == len(s)