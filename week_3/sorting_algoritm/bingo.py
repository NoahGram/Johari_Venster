def bingo_sort_3_arrays(arr1, arr2, arr3):
    def bingo_sort(arr):
        max_val = max(arr)
        min_val = min(arr)
        size = len(arr)
        # Create the buckets
        buckets = [0] * (max_val - min_val + 1)

        # Fill the buckets
        for num in arr:
            buckets[num - min_val] += 1

        # Fill the sorted array
        sorted_arr = []
        for i in range(len(buckets)):
            # Add the number of times the bucket's index appears in the array
            sorted_arr.extend([i + min_val] * buckets[i])

        return sorted_arr

    sorted_arr1 = bingo_sort(arr1)
    sorted_arr2 = bingo_sort(arr2)
    sorted_arr3 = bingo_sort(arr3)

    return sorted_arr1, sorted_arr2, sorted_arr3

# Example usage:
arr1 = [64, 34, 25, 12, 22, 11, 90, 54, 67, 29, 10, 43, 88, 91, 100, 23, 36, 48, 55, 77]
arr2 = [43, 21, 65, 90, 76, 88, 47, 33, 22, 99, 11, 7, 29, 85, 62, 50, 39, 20, 5, 74]
arr3 = [53, 36, 29, 41, 15, 77, 82, 19, 63, 48, 90, 22, 60, 10, 84, 35, 45, 75, 56, 38]

print("\n ( Bingo Sort ) \n")
print("Original arrays:")
print("Array 1:", arr1)
print("Array 2:", arr2)
print("Array 3:", arr3)

sorted_arr1, sorted_arr2, sorted_arr3 = bingo_sort_3_arrays(arr1, arr2, arr3)

print("\nSorted arrays:")
print("Array 1:", sorted_arr1)
print("Array 2:", sorted_arr2)
print("Array 3:", sorted_arr3)
