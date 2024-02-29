import random
import time
import numpy as np
from stack import Stack

def dutch_national_flag(data):
    # Initialize pointers for the three sections
    low = 0  # Pointer for 0s (Lowest value)
    mid = 0  # Pointer for 1s (middle value)
    high = len(data) - 1  # Pointer for 2s (Highest value)

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
    arr_numpy = np.random.randint(0, 3, size=100)
    print("Original array (NumPy):", arr_numpy)

    # Measure execution time for NumPy array
    start_time = time.perf_counter()
    sorted_arr_numpy = dutch_national_flag(arr_numpy.copy())  # Copy to avoid modifying the original array
    end_time = time.perf_counter()

    print("Array after sorting using Dutch National Flag algorithm (NumPy):", sorted_arr_numpy)
    execution_time_ms_numpy = (end_time - start_time) * 1000
    print("Execution time (NumPy):", execution_time_ms_numpy, "ms")

    # Test with a Python list
    arr_list = [random.randint(0, 2) for _ in range(100)]
    print("\nOriginal list (Python):", arr_list)

    # Measure execution time for Python list
    start_time = time.perf_counter()
    sorted_arr_list = dutch_national_flag(arr_list.copy())  # Copy to avoid modifying the original list
    end_time = time.perf_counter()

    print("List after sorting using Dutch National Flag algorithm (Python):", sorted_arr_list)
    execution_time_ms_list = (end_time - start_time) * 1000
    print("Execution time (Python):", execution_time_ms_list, "ms")

    # Test with a custom stack data structure
    arr_stack = Stack()
    for _ in range(100):
        arr_stack.push(random.randint(0, 2))
    print("\nOriginal stack (Custom Stack):", arr_stack.items)

    # Measure execution time for custom stack
    start_time = time.perf_counter()
    sorted_arr_stack = dutch_national_flag(arr_stack.items.copy())  # Copy to avoid modifying the original stack
    end_time = time.perf_counter()

    print("Stack after sorting using Dutch National Flag algorithm (Custom Stack):", sorted_arr_stack)
    execution_time_ms_stack = (end_time - start_time) * 1000
    print("Execution time (Custom Stack):", execution_time_ms_stack, "ms")
