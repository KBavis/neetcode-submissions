class Solution:
    def isValid(self, s: str) -> bool:
        

        mapping = {
            '}': '{',
            ']': '[',
            ')': '('
        }

        stack = []
        
        for curr in s:
            if curr in mapping:
                if not stack or stack.pop() != mapping[curr]:
                    return False 
            else:
                stack.append(curr)
        
        return not stack