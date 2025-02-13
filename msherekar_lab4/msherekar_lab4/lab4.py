from typing import TextIO
import textwrap
from msherekar_lab4.QuickSort_Counts import QuickSort
from msherekar_lab4.Hybrid_50Counts import HybridSort50
from msherekar_lab4.Hybrid_100Counts import HybridSort100
from msherekar_lab4.QuickSort_MedianCount import quicksort
from msherekar_lab4.MergeSort_Natural_LinkedList import linked_list_natural_merge_sort, LinkedList, Node, tolist


# This line of code connects input on command line to code under this function
def process_files(infile: TextIO, outfile1: TextIO, outfile2: TextIO, outfile3: TextIO, outfile4: TextIO,
                  outfile5: TextIO) -> None:
    # read data from the given infile i.e input file
    data = []
    for line in infile.readlines():
        data.append(int(line.strip()))

    outfile1.write("Sorting with QuickSort algorithm using median as the first element:" + "\n")
    # Writing the comparison and swaps from normal quick sort
    outfile1.write("The number of comparisons and swaps required to sort the given data are:"
                   + " " + textwrap.fill(str(QuickSort(data, 0, len(data) - 1))) + " " + "respectively." + "\n")
    # Writing sorted list by normal quick sort on the output file
    outfile1.write(str(data) + "\n")

    # Again reading the data because previous sort will sort the data in place
    for line in infile.readlines():
        data.append(int(line.strip()))

    outfile2.write("Sorting with a Hybrid of Quick & Insertion Sort using median as the first element and invoking "
                   "insertion sort when size of subarray is 50" + "\n")
    # Writing sorted list by hybrid(50) quick sort on the output file
    outfile2.write(str(data) + "\n")
    # Writing the comparison and swaps from hybrid(50) quick sort
    outfile2.write("The number of comparisons and swaps required to sort the given data are:"
                   + " " + textwrap.fill(str(HybridSort50(data, 0, len(data) - 1))) + " " + "respectively." + "\n")

    for line in infile.readlines():
        data.append(int(line.strip()))

    outfile3.write("Sorting with a Hybrid of Quick & Insertion Sort using median as the first element and invoking "
                   "insertion sort when size of subarray is 100" + "\n")
    # Writing sorted list by hybrid(100) quick sort on the output file
    outfile3.write(str(data) + "\n")
    # Writing the comparison and swaps from hybrid(100) quick sort
    outfile3.write("The number of comparisons and swaps required to sort the given data are:"
                   + " " + textwrap.fill(str(HybridSort100(data, 0, len(data) - 1))) + " " + "respectively." + "\n")

    for line in infile.readlines():
        data.append(int(line.strip()))

    outfile4.write("Sorting with Quick Sort algorithm  using median of three as a pivot"+ "\n")
    # Writing sorted list by quick sort with median of three as pivot on the output file
    outfile4.write(str(data) + "\n")
    # Writing comparisons and swaps from sort with median of three as pivot on the output file
    outfile4.write("The number of comparisons and swaps required to sort the given data are:"
                   + " " + textwrap.fill(str(quicksort(data, 0, len(data) - 1))) + " " + "respectively." + "\n")

    for line in infile.readlines():
        data.append(int(line.strip()))

    outfile5.write("Sorted with Natural Merge Algorithm with a Linked List implementation" + "\n")
    head = None
    for key in data:
        head = LinkedList(key, head)
    head = linked_list_natural_merge_sort(head)[0]
    comparisons = linked_list_natural_merge_sort(head)[1]
    swaps = linked_list_natural_merge_sort(head)[2]
    outfile5.write(textwrap.fill(str(tolist(head, -1))))
    outfile5.write("\n")
    outfile5.write("Number of comparisons:" + " " + str(comparisons) + "\n")
    outfile5.write("Number of swaps:" + " " + str(swaps) + "\n")
