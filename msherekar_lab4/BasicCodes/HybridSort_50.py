# Source: https://stackoverflow.com/questions/71083355/hybrid-algorithm-that-combines-insertion-sort-and-quick-sort
# Recursion implementation

from random import randint


def InsertionSort(data):
    """
    This method takes in a list and sort it using insertion sort
    :param data: name of the list
    :return: sorted (ascending) list of give data
    """
    # loop over all element of data starting at 1st element
    for i in range(1, len(data)):

        # key is element at index i or element at index i is stored in key variable
        key = data[i]
        j = i - 1

        while j >= 0 and key < data[j]:
            data[j + 1] = data[j]
            j = j - 1

        data[j + 1] = key


def PartitionIndex(data, lowIndex, highIndex):
    """
    This method returns index of new pivot for the subsequent run of quicksort
    :param data: name of the list to be sorted
    :param lowIndex: least index value, 0 generally
    :param highIndex: highest index value, len(data) - 1
    :return: new pivot position
    """
    # assign a variable to lowIndex i.e 0 generally
    pivotIndex = lowIndex

    # Which means pivot is at the lowest index i.e the first element of the list
    # This is the most salient point of this version of Quick Sort i.e Hoare Partition
    pivot = data[pivotIndex]

    while lowIndex < highIndex:
        # moving right
        while lowIndex < len(data) and data[lowIndex] <= pivot:
            lowIndex += 1

        # moving left
        while data[highIndex] > pivot:
            highIndex -= 1

        if lowIndex < highIndex:
            Swap(lowIndex, highIndex, data)

    # move the pivot to a new position
    Swap(pivotIndex, highIndex, data)

    # return new pivot
    return highIndex


def Swap(i, j, data):
    """
    this method swaps two elements in an array. One is at index (i) and other is at index(j)
    :param i:
    :param j:
    :param data:
    :return:
    """
    if i != j:
        temp = data[i]
        data[i] = data[j]
        data[j] = temp


def HybridSort(data, lowIndex=0, highIndex=None):
    """
    This method takes as input name of a list to be sorted, lower index number i.e 0 and higher index number as None
    :param highIndex:
    :param lowIndex:
    :param data:
    :return:
    """
    if highIndex is None:
        highIndex = len(data) - 1

    if lowIndex < highIndex:

        # if the size of sub array while partitioning is less than a threshold (50 in this case), invoke insertion sort
        if highIndex - lowIndex + 1 < 50:
            InsertionSort(data)
            return

        # if the size of the sub-array is greater than the threshold, invoke quicksort
        pivotIndex = PartitionIndex(data, lowIndex, highIndex)

        # Recursion call on hybrid sort
        HybridSort(data, lowIndex, pivotIndex - 1)
        HybridSort(data, pivotIndex + 1, highIndex)


if __name__ == '__main__':
    Array_Length = 1000
    random_list = [randint(0, 10000) for i in range(Array_Length)]
    HybridSort(random_list, 0, len(random_list)-1)
    print(random_list)
