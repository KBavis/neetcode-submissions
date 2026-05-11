class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        

        stack = [] 
        operators = {"+", "-", "/", "*"}

        for token in tokens: 

            if token in operators:
                o2 = int(stack.pop())
                o1 = int(stack.pop())

                match token:
                    case "+":
                        res = o1 + o2 
                    case "-":
                        res = o1 - o2 
                    case "/":
                        res = int(o1 / o2) 
                    case "*":
                        res = o1 * o2 
                
                stack.append(str(res))
            else:
                stack.append(token)
        

        return int(stack.pop()) if stack else -1