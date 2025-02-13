# Source: https://stackoverflow.com/questions/71083355/hybrid-algorithm-that-combines-insertion-sort-and-quick-sort
# Recursion implementation
import sys
from random import randint
from msherekar_lab4.InsertionSort_Counts import InsertionSort
from msherekar_lab4.QuickSort_Counts import QuickSort, PartitionIndex

sys.setrecursionlimit(10 ** 6)


def HybridSort50(data, lowIndex=0, highIndex=None):
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

        else:
            # if the size of the sub-array is greater than the threshold, invoke quicksort
            pivotIndex = PartitionIndex(data, lowIndex, highIndex)

            # Recursion call on hybrid sort
            QuickSort(data, lowIndex, pivotIndex[2] - 1)
            QuickSort(data, pivotIndex[2] + 1, highIndex)

            return pivotIndex[0], pivotIndex[1]


if __name__ == '__main__':
    Array_Length = 1000
    random_list = [randint(0, 10000) for i in range(Array_Length)]
    y = HybridSort50(random_list, 0, len(random_list) - 1)
    print(random_list)
    print("Comparisons: " + str(y[0]))
    print("Swaps: " + str(y[1]))
