# Python implementation of the above approach

from random import randint


# Function to perform the insertion sort
def insertion_sort(arr, low, n):
    for i in range(low + 1, n + 1):
        val = arr[i]
        j = i
        while j > low and arr[j - 1] > val:
            arr[j] = arr[j - 1]
            j -= 1
        arr[j] = val


# The following two functions are used
# to perform quicksort on the array.

# Partition function for quicksort
def partition(arr, low, high):
    pivot = arr[high]
    i = j = low
    for i in range(low, high):
        if arr[i] < pivot:
            arr[i], arr[j] = arr[j], arr[i]
            j += 1
    arr[j], arr[high] = arr[high], arr[j]
    return j


# Function to call the partition function
# and perform quick sort on the array
def quick_sort(arr, low, high):
    if low < high:
        pivot = partition(arr, low, high)
        quick_sort(arr, low, pivot - 1)
        quick_sort(arr, pivot + 1, high)
        return arr


# Hybrid function -> Quick + Insertion sort
def hybrid_quick_sort(arr, low, high):
    while low < high:

        # If the size of the array is less
        # than threshold apply insertion sort
        # and stop recursion
        if high - low + 1 < 100:
            insertion_sort(arr, low, high)
            break

        else:
            pivot = partition(arr, low, high)

            # Optimised quicksort which works on
            # the smaller arrays first

            # If the left side of the pivot
            # is less than right, sort left part
            # and move to the right part of the array
            if pivot - low < high - pivot:
                hybrid_quick_sort(arr, low, pivot - 1)
                low = pivot + 1
            else:
                # If the right side of pivot is less
                # than left, sort right side and
                # move to the left side
                hybrid_quick_sort(arr, pivot + 1, high)
                high = pivot - 1
    return

if __name__ == '__main__':
    Array_Length = 1000
    random_list = [randint(0, 1000) for i in range(Array_Length)]
    # random_list = [22, 11, 88, 66, 55, 77, 33, 44]
    print(hybrid_quick_sort(random_list, random_list[0], random_list[len(random_list) - 1]))
