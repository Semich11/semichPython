class Stack:

    def empty(self):
        if len(self.stack) == 0: return True
        return False
    #end

    def push(self, element):
        self.stack.append(element)
    #end

    def pop(self):
        if self.empty(): raise IndexError('Stack is empty')
        self.stack.pop(0)
    #end

    def __init__(self):
        self.stack = []
    #end

    def peek(self):
        if self.empty(): raise IndexError('Stack is empty')
        return self.stack[-1]
    #end
    def search(self, element):
        if element not in self.stack: return -1
        return self.stack.index(element)





