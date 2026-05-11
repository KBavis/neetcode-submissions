class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []
        # keeping running track of minimum values 
        

    def push(self, val: int) -> None:
        minVal = min(self.minStack[-1], val) if self.minStack else val
        self.stack.append(val)
        self.minStack.append(minVal)
        

    def pop(self) -> None:
        self.minStack.pop() 
        return self.stack.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.minStack[-1]

        
