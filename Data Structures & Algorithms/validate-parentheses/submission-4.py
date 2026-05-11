class Solution:
    def isValid(self, s: str) -> bool:
        
        x = len(s)
        if x % 2 != 0:
            return False 

        mapping = {
            '{': '}',
            '[': ']',
            '(': ')'
        }

        stack = [] 

        for i in range(len(s)):
            curr = s[i]

            if curr in mapping:
                stack.append(mapping[curr])
            else:
                if not stack:
                    return False 
                
                expected = stack.pop() 
                if expected != curr:
                    return False 
            
        return not stack 