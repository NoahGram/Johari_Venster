import numpy as np
import time

def dutch_national_flag(arr):
    # Initialize pointers for the three sections
    low = 0  # Pointer for 0s (Lowest value)
    mid = 0  # Pointer for 1s (middle value)
    high = len(arr) - 1  # Pointer for 2s (Higest value)

    # Traverse the array and split it into three sections
    while mid <= high:
        if arr[mid] == 0:
            # If the current element is 0, swap it with the element at the low index
            arr[low], arr[mid] = arr[mid], arr[low]
            # Move low and mid pointers to the right
            low += 1
            mid += 1
        elif arr[mid] == 1:
            # If the current element is 1, move mid pointer to the right
            mid += 1
        else:  # arr[mid] == 2
            # If the current element is 2, swap it with the element at the high index
            arr[mid], arr[high] = arr[high], arr[mid]
            # Move high pointer to the left
            high -= 1
    
    return arr


if __name__ == "__main__":
    arr = (np.random.rand(10) * 3).astype(int)
    print("Original array:", arr)

    # Measure execution time
    start_time = time.perf_counter()

    sorted_arr = dutch_national_flag(arr)
    print("Array after sorting using Dutch National Flag algorithm:", sorted_arr)

    end_time = time.perf_counter()

    # Calculate execution time
    execution_time_ms = (end_time - start_time) * 1000
    print("Merge sort execution time:", execution_time_ms, "ms")