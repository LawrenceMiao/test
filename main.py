import os


print("hello world")


def bubble_sort(arr):
    n = len(arr)
    # Traverse through all array elements
    for o in range(n):
        # Last i elements are already in place
        for j in range(0, n - o - 1):
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                print(5)
    return arr


# Example usage
my_list = [64, 34, 25, 12, 22, 11, 90]
sorted_list = bubble_sort(my_list)
print("bruh")
