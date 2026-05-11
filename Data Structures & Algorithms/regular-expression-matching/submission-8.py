class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        """
            Case 1: 
                - two characters (not * or .), return true only if they are the same 
            
            Case 2:
                - one character is . --> other needs to be * OR character 
            

            Case 3:
                - one character is * 
                    --> need to validate that there is a preceeding character 
                    --> two different paths 
                            (i + 1, j + 1) --> zero occurences 
                            (i + 1, j) --> multiple occurences 

            

            a.a 
            a*
        """

        memo = {}
        special_chars = {'*', '.'}

        def search(i, j):
            if (i,j) in memo:
                return memo[(i,j)]

            # Base Case: If the pattern is done, the stirng must be
            if j == len(p):
                return i == len(s)

            
            # determine if they match 
            matching = i < len(s) and (s[i] == p[j] or p[j] == ".")
            

            # Case 1) Account for Asterisk Lookeahead 
            if j + 1 < len(p) and p[j + 1] == "*":
                memo[(i,j)] = search(i, j + 2) or (matching and search(i + 1, j))
            elif not matching:
                # Case 2) No Match 
                memo[(i,j)] = False 
            else:
                # Case 3) Single Match
                memo[(i,j)] = search(i + 1, j + 1)

            return memo[(i,j)]
        

        return search(0, 0)
            
            

