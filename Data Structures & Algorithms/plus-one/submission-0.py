class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        """
            start in reversed order 

            add one to current value 

            curr value // 10 = carry 
            curr value % 10 = new position at current point 

            continue while carry > 0 
        """


        i = len(digits) - 1 
        res = [] 

        carry = 1 
        while carry > 0 or i >= 0: 

            curr_val = digits[i] if i >= 0 else 0 
            curr_val += carry 

            remain = curr_val % 10 
            carry = curr_val // 10 

            res.append(remain)

            i -= 1
        
        return list(reversed(res))