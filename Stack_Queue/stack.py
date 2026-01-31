class Stack:
    def __init__(self):
        self._data = []

    def push(self, item):
        self._data.append(item)

    def pop(self):
        return self._data.pop()

    def peek(self):
        return self._data[-1]


stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print(stack.peek())
print(stack.pop())
