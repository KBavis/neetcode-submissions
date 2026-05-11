class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        self.res = [] 
        self.backtrack([], 0, 0, n)
        return self.res

    
    def backtrack(self, curr, open_parans, closed_parans, n):

        if open_parans == n and closed_parans == n:
            solution = "".join(curr)
            self.res.append(solution)
            return 
        

        if open_parans < n:
            curr.append('(')
            self.backtrack(curr, open_parans + 1, closed_parans, n)
            curr.pop()

        if closed_parans < n and closed_parans < open_parans:
            curr.append(')')
            self.backtrack(curr, open_parans, closed_parans + 1, n)
            curr.pop()
