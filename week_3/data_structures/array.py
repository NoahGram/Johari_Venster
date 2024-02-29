import random
import time
import numpy as np

def merge_sort(arr):
    #If the array has 1 or 0 elements, it is already sorted
    if len(arr) <= 1:  
        return arr

    # Split the array in half and sort each half
    mid = len(arr) // 2  
    left_half = merge_sort(arr[:mid])  
    right_half = merge_sort(arr[mid:])  

    sorted_arr = []
    i = j = 0

    # Merge the sorted halves
    while i < len(left_half) and j < len(right_half):
        # Compare the first elements of the two halves
        if left_half[i] < right_half[j]:
            sorted_arr.append(left_half[i])
            i += 1
        # If the right half element is smaller, append it to the sorted array
        else:
            sorted_arr.append(right_half[j])
            j += 1

    # Append the remaining elements of the left and right halves
    sorted_arr.extend(left_half[i:])
    sorted_arr.extend(right_half[j:])

    return sorted_arr

random_array = (np.random.randint(0, 100, 100))

print("\n ( Array Data Structure ) \n\nRandom array before sorting:", random_array)

# Measure execution time
start_time = time.perf_counter()

# Sort the random array using merge sort
sorted_array = merge_sort(random_array)

end_time = time.perf_counter()

# Calculate execution time
execution_time_ms = (end_time - start_time) * 1000

print("Sorted array:", sorted_array)
print("Merge sort execution time:", execution_time_ms, "ms")
