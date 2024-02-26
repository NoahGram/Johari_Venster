def gnome_sort_3_arrays(arr1, arr2, arr3):
    def gnome_sort(arr):
        index = 0
        n = len(arr)

        # Traverse the array
        while index < n:
            if index == 0:
                index += 1
            if arr[index] >= arr[index - 1]:
                # no swap, move to the next element
                index += 1
            else:
                # swap the elements
                arr[index], arr[index - 1] = arr[index - 1], arr[index]
                index -= 1

        return arr

    sorted_arr1 = gnome_sort(arr1)
    sorted_arr2 = gnome_sort(arr2)
    sorted_arr3 = gnome_sort(arr3)

    return sorted_arr1, sorted_arr2, sorted_arr3

# Example usage:
arr1 = [64, 34, 25, 12, 22, 11, 90, 54, 67, 29, 10, 43, 88, 91, 100, 23, 36, 48, 55, 77]
arr2 = [43, 21, 65, 90, 76, 88, 47, 33, 22, 99, 11, 7, 29, 85, 62, 50, 39, 20, 5, 74]
arr3 = [53, 36, 29, 41, 15, 77, 82, 19, 63, 48, 90, 22, 60, 10, 84, 35, 45, 75, 56, 38]


print("\n ( Gnome Sort ) \n")
print("Original arrays:")
print("Array 1:", arr1)
print("Array 2:", arr2)
print("Array 3:", arr3)

sorted_arr1, sorted_arr2, sorted_arr3 = gnome_sort_3_arrays(arr1, arr2, arr3)

print("\nSorted arrays:")
print("Array 1:", sorted_arr1)
print("Array 2:", sorted_arr2)
print("Array 3:", sorted_arr3)
