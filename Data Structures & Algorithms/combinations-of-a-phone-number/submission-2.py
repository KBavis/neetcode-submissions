class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        """
            a) Need mapping of an individual digit to its corresponding letters 
            b) Permutations sort of problem, need to track current "idx" 

            recursion:
                idx within digits 
                get current digit 
                get associated letters to that digit 
                iterate through digits 
                select one, and backtrack 
        """



        mapping = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"]
        }

        res = []
        if not digits:
            return res

        def permute(idx, soFar):
            if idx == len(digits):
                total = "".join(soFar)
                res.append(total)
                return 
            

            curr_digit = digits[idx]
            letters = mapping.get(curr_digit, [])

            for curr_letter in letters:
                soFar.append(curr_letter)
                permute(idx + 1, soFar)
                soFar.pop() 
        

        permute(0, [])
        return res 

        


    
        