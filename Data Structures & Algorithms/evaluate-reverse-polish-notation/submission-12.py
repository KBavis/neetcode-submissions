class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        operands = {"*", "-", "+", "/"}

        stack = []

        for token in tokens:

            if token not in operands:
                stack.append(int(token))
            else:

                n2 = stack.pop()
                n1 = stack.pop() 

                res = 0
                match token:
                    case "*":
                        res = n1 * n2
                    case "-":
                        res = n1 - n2 
                    case "+":
                        res = n1 + n2 
                    case "/":
                        res = int(n1 / n2)
                

                stack.append(res)
        

        return stack[0]
                    