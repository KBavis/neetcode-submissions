class Solution:
    def isPalindrome(self, s: str) -> bool:
        

        word = "".join(c.lower() for c in s if c.isalnum())


        stack = [] 
        mid = len(word) // 2

        for i in range(0, mid):
            stack.append(word[i])

        start = mid + 1 if len(word) % 2 != 0 else mid

        for i in range(start, len(word)):
            if stack.pop() != word[i]:
                return False 
        

        return True if not stack else False


