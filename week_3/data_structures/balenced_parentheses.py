import time
from stack import Stack

#Balenced Parentheses Algorithm
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