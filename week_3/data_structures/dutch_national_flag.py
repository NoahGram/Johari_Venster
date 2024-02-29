import numpy as np
import time
from stack import Stack

import time
from stack import Stack

def dutch_national_flag(data):
    # Initialize pointers for the three sections
    low = 0
    mid = 0
    high = len(data) - 1

    # Traverse the array and split it into three sections
    while mid <= high:
        if data[mid] == 0:
            # If the current element is 0, swap it with the element at the low index
            data[low], data[mid] = data[mid], data[low]
            # Move low and mid pointers to the right
            low += 1
            mid += 1
        elif data[mid] == 1:
            # If the current element is 1, move mid pointer to the right
            mid += 1
        else:  # data[mid] == 2
            # If the current element is 2, swap it with the element at the high index
            data[mid], data[high] = data[high], data[mid]
            # Move high pointer to the left
            high -= 1
    
    return data

if __name__ == "__main__":
    # Test with a NumPy array
    arr = [2, 0, 1, 2, 0, 1, 1, 0, 2, 2]
    print("\nOriginal array (Python List):", arr)

    # Measure execution time
    start_time = time.perf_counter()
    sorted_arr = dutch_national_flag(arr)
    end_time = time.perf_counter()

    print("Array after sorting using Dutch National Flag algorithm (Python List):", sorted_arr)
    execution_time_ms = (end_time - start_time) * 1000
    print("Execution time:", execution_time_ms, "ms")

    # Test with a Python list
    my_list = [2, 1, 0, 2, 1, 0, 1, 2, 0, 1]
    print("\nOriginal list (Python List):", my_list)

    # Measure execution time
    start_time = time.perf_counter()
    sorted_list = dutch_national_flag(my_list)
    end_time = time.perf_counter()

    print("List after sorting using Dutch National Flag algorithm (Python List):", sorted_list)
    execution_time_ms = (end_time - start_time) * 1000
    print("Execution time:", execution_time_ms, "ms")

    # Test with a custom stack data structure
    my_stack = Stack()
    my_stack.push(2)
    my_stack.push(1)
    my_stack.push(0)
    my_stack.push(2)
    my_stack.push(1)
    my_stack.push(0)
    print("\nOriginal stack (Custom Stack):", my_stack.items)

    # Measure execution time
    start_time = time.perf_counter()
    sorted_stack = dutch_national_flag(my_stack.items)
    end_time = time.perf_counter()

    print("Stack after sorting using Dutch National Flag algorithm (Custom Stack):", sorted_stack)
    execution_time_ms = (end_time - start_time) * 1000
    print("Execution time:", execution_time_ms, "ms")
