class Stack:
    # Constructor
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    # Add an item to the top of the stack
    def push(self, item):
        self.items.append(item)

    # Remove and return the top item from the stack
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return None

    # Return the top item from the stack
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return None

    # Return the number of items in the stack
    def size(self):
        return len(self.items)