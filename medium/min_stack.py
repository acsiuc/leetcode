
class MinStack:

    def __init__(self):
        self.stack = []
        self.minimums = {0: float('inf')}

    def push(self, val: int) -> None:
        self.stack.append(val)

        self.minimums[len(self.stack)] = min(self.minimums[len(self.stack) - 1], val)
        print(self.minimums[len(self.stack)]) 

    def pop(self) -> None:

        del self.stack[-1]

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        if self.minimums[len(self.stack)]!= float('inf'):
            return self.minimums[len(self.stack)]
        else:
            return None

if __name__ == "__main__":
    minStack = MinStack();
    print(minStack.push(1))
    print(minStack.push(2))
    print(minStack.push(0))
    print(minStack.getMin())
    print(minStack.pop())
    print(minStack.top())    
    print(minStack.getMin())