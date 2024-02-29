import random
import time
import numpy as np
from stack import Stack

def merge_sort(data):
    # Convert the input data to a list if it's not already
    if not isinstance(data, list):
        data = list(data)

    #If the list has 1 or 0 elements, it is already sorted
    if len(data) <= 1:  
        return data

    # Split the list in half and sort each half
    mid = len(data) // 2  
    left_half = merge_sort(data[:mid])  
    right_half = merge_sort(data[mid:])  

    sorted_data = []
    i = j = 0

    # Merge the sorted halves
    while i < len(left_half) and j < len(right_half):
        # Compare the first elements of the two halves
        if left_half[i] < right_half[j]:
            sorted_data.append(left_half[i])
            i += 1
        # If the right half element is smaller, append it to the sorted list
        else:
            sorted_data.append(right_half[j])
            j += 1

    # Append the remaining elements of the left and right halves
    sorted_data.extend(left_half[i:])
    sorted_data.extend(right_half[j:])

    return sorted_data

if __name__ == "__main__":
    # Test with different data structures: list, stack, and numpy array
    random_list = [random.randint(0, 100) for _ in range(100)]
    random_stack = Stack()
    for num in random_list:
        random_stack.push(num)
    random_array = np.array(random_list)

    # Measure execution time for list
    start_time = time.perf_counter()
    sorted_list = merge_sort(random_list)
    end_time = time.perf_counter()
    execution_time_ms = (end_time - start_time) * 1000
    print("\n(List Data Structure)")
    print("Sorted list:", sorted_list)
    print("Merge sort execution time:", execution_time_ms, "ms")

    # Measure execution time for stack
    start_time = time.perf_counter()
    sorted_stack = merge_sort(random_stack.items)
    end_time = time.perf_counter()
    execution_time_ms = (end_time - start_time) * 1000
    print("\n(Stack Data Structure)")
    print("Sorted stack:", sorted_stack)
    print("Merge sort execution time:", execution_time_ms, "ms")

    # Measure execution time for numpy array
    start_time = time.perf_counter()
    sorted_array = merge_sort(random_array)
    end_time = time.perf_counter()
    execution_time_ms = (end_time - start_time) * 1000
    print("\n(Numpy Array Data Structure)")
    print("Sorted array:", sorted_array)
    print("Merge sort execution time:", execution_time_ms, "ms")