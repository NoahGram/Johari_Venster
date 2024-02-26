import time

def bubbbleSort3Arrays(arr1, arr2, arr3):    
    def bubbleSort(arr):
        n = len(arr)
        for i in range(n-1):
            swapped = False
            # Traverse through all array elements and swap if greater than the next element
            for j in range(0, n-i-1):
                if arr[j] > arr[j + 1]:
                    swapped = True
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
            
            # If no two elements were swapped, then break
            if not swapped:
                break
        return arr

    sorted_arr1 = bubbleSort(arr1)
    sorted_arr2 = bubbleSort(arr2)
    sorted_arr3 = bubbleSort(arr3)

    return sorted_arr1, sorted_arr2, sorted_arr3

arr1 = [64, 34, 25, 12, 22, 11, 90, 54, 67, 29, 10, 43, 88, 91, 100, 23, 36, 48, 55, 77]
arr2 = [43, 21, 65, 90, 76, 88, 47, 33, 22, 99, 11, 7, 29, 85, 62, 50, 39, 20, 5, 74]
arr3 = [53, 36, 29, 41, 15, 77, 82, 19, 63, 48, 90, 22, 60, 10, 84, 35, 45, 75, 56, 38]

start_time = time.time()
sorted_arr1, sorted_arr2, sorted_arr3 = bubbbleSort3Arrays(arr1, arr2, arr3)
end_time = time.time()

# Calculate elapsed time in milliseconds
elapsed_time_ms = (end_time - start_time) * 1000

print("\n( Bubble Sort )\n")
print("Original arrays:")
print("Array 1:", arr1)
print("Array 2:", arr2)
print("Array 3:", arr3)

print("\nSorted arrays:")
print("Array 1:", sorted_arr1)
print("Array 2:", sorted_arr2)
print("Array 3:", sorted_arr3)

print("\nTime taken for sorting:", elapsed_time_ms, "seconds")
