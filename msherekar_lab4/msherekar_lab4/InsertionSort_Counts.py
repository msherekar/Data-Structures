# Source: https://realpython.com/sorting-algorithms-python/#the-insertion-sort-algorithm-in-python
from random import randint


def InsertionSort(data):
    """
    This function takes in a array (list) of data and sorts it in ascending order using insertion sort algorithm
    :param data: name of the list
    :return: sorted list
    """
    comp = 0
    swap = 0

    # Loop from the second element of the array until the last element
    for i in range(1, len(data)):

        # This is the element we want to position in its correct place
        key_item = data[i]

        # Initialize the variable that will be used to find the correct position of the element referenced by `key_item`
        j = i - 1

        # Run through the list of items (the left portion of the array) and find the correct position of the element
        # referenced by `key_item`. Do this only if `key_item` is smaller than its adjacent values.
        comp += 1
        while j >= 0 and data[j] > key_item:
            # Shift the value one position to the left and reposition j to point to the next element (from right to left
            data[j + 1] = data[j]
            j -= 1
            comp += 1
            swap += 1

        # When you finish shifting the elements, you can position `key_item` in its correct location
        data[j + 1] = key_item

    return data, comp, swap


if __name__ == '__main__':
    Array_Length = 5000
    random_list = [randint(0, 100000) for i in range(Array_Length)]
    #random_list = [2, 1 , 3, 4, 5, 6, 7, 8, 9, 10]
    print(InsertionSort(random_list)[0])
    print("comparisons:")
    print(InsertionSort(random_list)[1])
    print("swaps:")
    print(InsertionSort(random_list)[2])

