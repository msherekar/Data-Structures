from typing import TextIO
import sys
import os
from QuickSort_Counts import QuickSort
from Hybrid_50Counts import HybridSort50
from Hybrid_100Counts import HybridSort100
from QuickSort_MedianCount import quicksort
from MergeSort_Natural_LinkedList import linked_list_natural_merge_sort, LinkedList, Node, tolist


def process_folders(InFolder: TextIO) -> None:
    files = []
    for file_name in os.listdir(InFolder):
        if file_name.endswith('.txt'):
            files.append(file_name)

    for file in files:

        # how to give correct path of output folder to save output file
        # how to give correct path of file???
        with open(file, mode="r") as in_file:
            data = []
            for line in in_file.readlines():
                data.append(int(line.strip()))

        with open("Output_File.txt", mode="a") as Output_File:
            Output_File.write("File" + " " + file + " " + "is sorted by various sorting algorithm as follows" + "\n")

            Output_File.write("QuickSort:" + "\n")
            # Writing the comparison and swaps from normal quick sort
            Output_File.write("The number of comparisons and swaps required to sort the given data are:"
                              + " " + str(QuickSort(data, 0, len(data) - 1)) + " " + "respectively." + "\n")
            # Writing sorted list by normal quick sort on the output file
            Output_File.write(str(data) + "\n")

            Output_File.write("\n")
            Output_File.write("Hybrid QuickSort with threshold of 50:" + "\n")
            # Writing sorted list by hybrid(50) quick sort on the output file
            Output_File.write(str(data) + "\n")
            # Writing the comparison and swaps from hybrid(50) quick sort
            Output_File.write("The number of comparisons and swaps required to sort the given data are:"
                              + " " + str(HybridSort50(data, 0, len(data) - 1)) + " " + "respectively." + "\n")

            Output_File.write("\n")
            Output_File.write("Hybrid QuickSort with threshold of 100:" + "\n")
            # Writing sorted list by hybrid(100) quick sort on the output file
            Output_File.write(str(data) + "\n")
            # Writing the comparison and swaps from hybrid(100) quick sort
            Output_File.write("The number of comparisons and swaps required to sort the given data are:"
                              + " " + str(HybridSort100(data, 0, len(data) - 1)) + " " + "respectively." + "\n")

            Output_File.write("\n")
            Output_File.write("QuickSort with Median of 3 as Pivot:" + "\n")
            # Writing sorted list by quick sort with median of three as pivot on the output file
            Output_File.write(str(data) + "\n")
            # Writing comparisons and swaps from sort with median of three as pivot on the output file
            Output_File.write("The number of comparisons and swaps required to sort the given data are:"
                              + " " + str(quicksort(data, 0, len(data) - 1)) + " " + "respectively." + "\n")

            Output_File.write("\n")
            Output_File.write("The data sorted by Natural Merge Sort with Linked List implementation: " + "\n")
            head = None
            for key in data:
                head = LinkedList(key, head)
            head = linked_list_natural_merge_sort(head)[0]
            comparisons = linked_list_natural_merge_sort(head)[1]
            swaps = linked_list_natural_merge_sort(head)[2]
            Output_File.write(str(tolist(head, -1)))
            Output_File.write("\n")
            Output_File.write("Number of comparisons:" + " " + str(comparisons) + "\n")
            Output_File.write("Number of swaps:" + " " + str(swaps) + "\n")
            Output_File.write("\n")

    return


# wont work from terminal if not for this line of code
process_folders('/Users/mukulsherekar/PycharmProjects/DS/msherekar_lab4/resources/input')
# process_folders(InFolder: TextIO)
