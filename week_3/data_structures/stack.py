import time

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

def is_balanced(parentheses):
    # Create a stack to store the opening parentheses
    stack = Stack()

    # Iterate through the input string
    for paren in parentheses:
        # If the current character is an opening parenthesis, push it onto the stack
        if paren in '({[':
            stack.push(paren)
        elif paren in ')}]':
            # If the stack is empty, no corresponding opening parenthesis for the current closing parenthesis,
            if stack.is_empty():
                return False
            # If the current closing parenthesis does not match the top of the stack, the string is not balanced
            else:
                # Remove the top item from the stack
                top = stack.pop()
                if (paren == ')' and top != '(') or \
                   (paren == '}' and top != '{') or \
                   (paren == ']' and top != '['):
                    return False

    return stack.is_empty()


if __name__ == "__main__":
    test_cases = ["()", "()[]{}", "(]", "([)]", "{[]}", "((())", "((((((()))))))"]

    # Measure execution time
    start_time = time.perf_counter()

    for test_case in test_cases:
        print(f"'{test_case}' is balanced: {is_balanced(test_case)}")

    end_time = time.perf_counter()

    # Calculate execution time
    execution_time_ms = (end_time - start_time) * 1000
    print("Merge sort execution time:", execution_time_ms, "ms")