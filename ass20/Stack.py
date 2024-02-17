class Stack:
    def __init__(self):
        self.stack = []

    #TODO Use list append method to add element
    def push(self, item):
       self.stack.append(item)

    #TODO Use list pop method to remove element
    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            print("Stack is empty. Cannot pop from an empty stack.")
            return None

    def is_empty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)