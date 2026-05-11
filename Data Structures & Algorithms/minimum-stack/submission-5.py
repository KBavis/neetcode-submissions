class MinStack:

    def __init__(self):
        self.stack = [] 
        self.min_stack = []
        

    def push(self, val: int) -> None:
        min_val = min(val, self.min_stack[-1]) if self.min_stack else val
        self.stack.append(val)
        self.min_stack.append(min_val)
        

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()
        

    def top(self) -> int:
        return self.stack[-1] if self.stack else None 
        

    def getMin(self) -> int:
        return self.min_stack[-1] if self.min_stack else None 
        
