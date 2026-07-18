class MinStack:

    def __init__(self):
        # need one stack to maintain stack and mins to maintain minstack
        self.stack=[]
        self.mins=[]

    def push(self, val: int) -> None:
        # append val to stack
        self.stack.append(val)
        # min value in the min stack
        val=min(val,self.mins[-1] if self.mins else val)
        self.mins.append(val)

    def pop(self) -> None:
        # remove value from stacks
        self.stack.pop()
        self.mins.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.mins[-1]
