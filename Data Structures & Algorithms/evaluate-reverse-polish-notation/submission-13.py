class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        

        stack = [] 
        operands = {'+', '-', '*', '/'}

        for i in range(len(tokens)):
            token = tokens[i]

            if token in operands:
                n2 = int(stack.pop())
                n1 = int(stack.pop())
                
                match token:
                    case '+':
                        stack.append(n1 + n2)
                    case '-':
                        stack.append(n1 - n2)
                    case '/':
                        stack.append(n1 / n2)
                    case '*':
                        stack.append(n1 * n2)
            else:
                stack.append(token)
        
        return int(stack[-1])