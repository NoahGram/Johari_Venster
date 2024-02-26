import random

def pigeonhole_sort(provided):
    
    # Find minimum and maximum values in array. Let the minimum and maximum values be ‘min’ and ‘max’ respectively. 
    min_value = min(provided)
    max_value = max(provided)

    # Also find range as ‘max-min+1’. 
    range_buh = max_value - min_value + 1

    # Set up an array of initially empty “pigeonholes” the same size as of the range.
    pigeonhole = [0] * range_buh

    # Iterate through each array element and place it in the corresponding pigeonhole.
    for i in range(len(provided)):
        pigeonhole[provided[i]-min_value] += 1

    # Iterate through each pigeonhole element and place all the elements back into the array.
    index = 0
    for i in range(range_buh):
        while pigeonhole[i] > 0:
            pigeonhole[i] -= 1
            provided[index] = i + min_value
            index += 1

    return provided

# Randomized test case
initial = [random.randint(0, 20) for i in range(20)]

print("\n ( Pigeonhole Sorting ) \n")
print("Initial array:", initial)
print("Sorted array:", pigeonhole_sort(initial), "\n")