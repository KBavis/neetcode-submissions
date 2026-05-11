class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set() 

        while n not in seen:
            seen.add(n)

            val = str(n)
            curr = 0 

            for i in range(len(val)):
                curr += int(val[i])**2
            
            if curr == 1:
                return True 
            
            n = curr 
        

        return False 