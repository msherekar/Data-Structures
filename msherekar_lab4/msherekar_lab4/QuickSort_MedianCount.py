# Source: https://stackoverflow.com/questions/50912873/python-quicksort-with-median-of-three
# Pivot is median of elements at first, last and middle indices of an array.
# Recursion implementation

from random import randint
import statistics


def middleIndex(data):
    middle = float(len(data)) / 2
    if middle % 2 != 0:
        return data[int(middle - 0.5)]
    else:
        return data[int(middle - 1)]


def partition(A, low, high):
    c = 0 # c = comparisons
    s = 0 # s= swaps

    m1 = A[low]
    m2 = middleIndex(A)
    m3 = A[high]

    median = statistics.median([m1, m2, m3])

    pivotindex = A.index(median)

    A[low], A[pivotindex] = A[pivotindex], A[low]
    s = s+1

    pivot = A[low]

    i = low

    for j in range(low + 1, high + 1):
        if (A[j] < pivot):
            c = c + 1
            i = i + 1
            A[i], A[j] = A[j], A[i]
            s = s+1
    A[i], A[low] = A[low], A[i]
    s = s+1

    return i, c, s


def quicksort(A, low, high):
    if low < high:
        m,c,s = partition(A, low, high)
        (lc, ls) = quicksort(A, low, m - 1)
        (rc, rs) = quicksort(A, m + 1, high)
        return c+lc+rc, s+ls+rs
    return (0,0)


if __name__ == '__main__':
    x = [randint(0, 10000) for i in range(100)]
    print(quicksort(x, 0, len(x)-1))
    print(x)



