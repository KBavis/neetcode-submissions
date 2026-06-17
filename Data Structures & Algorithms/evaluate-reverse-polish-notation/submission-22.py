class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = [] 
        operators = {"+", "-", "*", "/"}
        for i in range(len(tokens)):

            curr_token = tokens[i]
            if curr_token in operators:
                op_2 = stack.pop()
                op_1 = stack.pop() 

                if curr_token == "*":
                    res = op_1 * op_2
                elif curr_token == "/":
                    res = op_1 / op_2
                elif curr_token == "+":
                    res = op_1 + op_2
                else:
                    res = op_1 - op_2 
                
                stack.append(int(res))
            else:
                stack.append(int(curr_token))
        

        return stack[0]