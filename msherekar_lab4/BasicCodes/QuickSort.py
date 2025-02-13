# Pivot is the first element of data (Hoare Partition)
# Recursion implementation
from random import randint


def QuickSort(data, lowIndex, highIndex):
    """
    This method sorts the data using quick sort algorithm using first element as pivot.
    :param data: name of the list
    :param lowIndex: least index value, 0 generally
    :param highIndex: highest index value, len(data) - 1
    :return: sorted (ascending) list
    """
    # As long as lower index is smaller than higher index
    if lowIndex < highIndex:
        # find a new pivot ie find a new index which has the pivot
        pivotIndex = PartitionIndex(data, lowIndex, highIndex)

        # Recursive call on left sub array starting from beginning to one element before pivot
        QuickSort(data, lowIndex, pivotIndex - 1)

        # Recursive call on right sub array starting from first element after the pivot to the end
        QuickSort(data, pivotIndex + 1, highIndex)

        # no return because list is itself being sorted without being stored anywhere.


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


if __name__ == '__main__':
    Array_Length = 100
    random_list = [randint(0, 1000) for i in range(Array_Length)]
    #random_list = [22, 11, 88, 66, 55, 77, 33, 44]
    QuickSort(random_list, 0, len(random_list)-1)
    print(random_list)
