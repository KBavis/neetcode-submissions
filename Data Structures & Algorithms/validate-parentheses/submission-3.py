class Solution:
    def isValid(self, s: str) -> bool:
        
        if not s:
            return True 
        elif len(s) % 2 != 0:
            return False


        mapping = {
            "[": "]",
            "{": "}",
            "(" : ")"
        }

        stack = [] 
        for c in s:
            if c in mapping:
                stack.append(mapping[c])
            else:
                if not stack or stack.pop() != c:
                    return False 
                

        return not stack 