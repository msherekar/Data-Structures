# Source: https://stackoverflow.com/questions/71083355/hybrid-algorithm-that-combines-insertion-sort-and-quick-sort


from random import randint


def QuickSort(data, lowIndex, highIndex):
    """
    This method sorts the data using quick sort algorithm using first element as pivot (Hoare Partition).
    :param data: name of the list
    :param lowIndex: least index value, 0 generally
    :param highIndex: highest index value, len(data) - 1
    :return: sorted list, number of comparisons and swaps
    """
    # As long as lower index is smaller than higher index
    if lowIndex < highIndex:
        # find a new pivot ie find a new index which has the pivot
        (comparisons, swaps, pivotIndex) = PartitionIndex(data, lowIndex, highIndex)

        # Recursive call on left sub array starting from beginning to one element before pivot
        (left_comparisons, left_swaps) = QuickSort(data, lowIndex, pivotIndex - 1)

        # Recursive call on right sub array starting from first element after the pivot to the end
        (right_comparisons, right_swaps) = QuickSort(data, pivotIndex + 1, highIndex)

        return comparisons + left_comparisons + right_comparisons, swaps + left_swaps + right_swaps

    return 0, 0
    # return data?
    # no return because list is itself being sorted without being stored anywhere.


def PartitionIndex(data, lowIndex, highIndex):
    """
    This method returns index of new pivot for the subsequent run of quicksort
    :param data: name of the list to be sorted
    :param lowIndex: least index value, 0 generally
    :param highIndex: highest index value, len(data) - 1
    :return: new pivot position
    """
    comparisons = 0
    swaps = 0

    # assign a variable to lowIndex i.e 0 generally
    pivotIndex = lowIndex

    # Which means pivot is at the lowest index i.e the first element of the list
    # This is the most salient point of this version of Quick Sort i.e Hoare Partition
    pivot = data[pivotIndex]

    while lowIndex < highIndex:
        # moving right
        while lowIndex < len(data) and data[lowIndex] <= pivot:
            comparisons += 1
            lowIndex += 1

        # moving left
        while data[highIndex] > pivot:
            comparisons += 1
            highIndex -= 1

        if lowIndex < highIndex:
            Swap(lowIndex, highIndex, data)
            swaps += 1

    # move the pivot to a new position
    Swap(pivotIndex, highIndex, data)
    swaps += 1

    # return new pivot
    return comparisons, swaps, highIndex


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
    with open("descending50.txt", mode="r") as in_file:
        data = []
        for line in in_file.readlines():
            data.append(int(line.strip()))

        print(QuickSort(data, 0, len(data) - 1))
        print(data)

    Array_Length = 50
    random_list = [randint(0, 1000) for i in range(Array_Length)]
    # random_list = [22, 11, 88, 66, 55, 77, 33, 44]
    print(QuickSort(random_list, 0, len(random_list) - 1))
    print(random_list)
    print("Comparisons: " + str(QuickSort(random_list, 0, len(random_list) - 1)[0]))
    print("Swaps: " + str(QuickSort(random_list, 0, len(random_list) - 1)[1]))
