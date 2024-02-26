def cocktail_sort_3_arrays(arr1, arr2, arr3):
    def cocktail_sort(arr):
        n = len(arr)
        swapped = True
        start = 0
        end = n - 1

        while swapped:
            swapped = False
            # Forward bubble sort
            for i in range(start, end):
                if arr[i] > arr[i + 1]:
                    arr[i], arr[i + 1] = arr[i + 1], arr[i]
                    swapped = True

            if not swapped:
                break

            swapped = False
            end -= 1
            # Backward bubble sort
            for i in range(end - 1, start - 1, -1):
                if arr[i] > arr[i + 1]:
                    arr[i], arr[i + 1] = arr[i + 1], arr[i]
                    swapped = True

            start += 1

        return arr

    sorted_arr1 = cocktail_sort(arr1)
    sorted_arr2 = cocktail_sort(arr2)
    sorted_arr3 = cocktail_sort(arr3)

    return sorted_arr1, sorted_arr2, sorted_arr3

# Example usage:
arr1 = [64, 34, 25, 12, 22, 11, 90, 54, 67, 29, 10, 43, 88, 91, 100, 23, 36, 48, 55, 77]
arr2 = [43, 21, 65, 90, 76, 88, 47, 33, 22, 99, 11, 7, 29, 85, 62, 50, 39, 20, 5, 74]
arr3 = [53, 36, 29, 41, 15, 77, 82, 19, 63, 48, 90, 22, 60, 10, 84, 35, 45, 75, 56, 38]

print("Original arrays:")
print("Array 1:", arr1)
print("Array 2:", arr2)
print("Array 3:", arr3)

sorted_arr1, sorted_arr2, sorted_arr3 = cocktail_sort_3_arrays(arr1, arr2, arr3)

print("\nSorted arrays:")
print("Array 1:", sorted_arr1)
print("Array 2:", sorted_arr2)
print("Array 3:", sorted_arr3)
