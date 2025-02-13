from QuickSort_Counts import QuickSort
from Hybrid_50Counts import HybridSort50
from Hybrid_100Counts import HybridSort100
from QuickSort_MedianCount import quicksort
from MergeSort_Natural_LinkedList import linked_list_natural_merge_sort, LinkedList, Node, printList


with open("Output_File.txt", mode="a") as Output_File:
    with open("random50.txt", mode="r") as RandomOrder_File:
        random = []
        for line in RandomOrder_File.readlines():
            line.strip()
            random.append(int(line.strip()))
        Output_File.write("The random ordered data is: " + "\n")
        Output_File.write(str(random) + "\n")
        Output_File.write("The data sorted by Quick Sort is: " + "\n")
        Output_File.write(str(QuickSort(random, 0, len(random)-1)) + "\n")
        Output_File.write("The data sorted by Hybrid Sort with 50 threshold is: " + "\n")
        Output_File.write(str(HybridSort50(random, 0, len(random) - 1)) + "\n")
        Output_File.write("The data sorted by Hybrid Sort with 100 threshold is: " + "\n")
        Output_File.write(str(HybridSort100(random, 0, len(random) - 1)) + "\n")
        Output_File.write("The data sorted by Quick Sort with median of 3 as pivot: " + "\n")
        Output_File.write(str(quicksort(random, 0, len(random) - 1)) + "\n")

        head = None
        for key in random:
            head = LinkedList(key, head)
        head = linked_list_natural_merge_sort(head)[0]
        comparisons = linked_list_natural_merge_sort(head)[1]
        swaps = linked_list_natural_merge_sort(head)[2]
        Output_File.write("The data sorted by Natural Merge Sort with Linked List implementation: " + "\n")
        #Output_File.write(printList(head))
        Output_File.write(str(comparisons))
        Output_File.write(str(swaps))

    with open("descending50.txt", mode="r") as DescendingOrder_File:
        dsc = []
        for line in DescendingOrder_File.readlines():
            line.strip()
            dsc.append(int(line.strip()))
        Output_File.write("The descending ordered data is: " + "\n")
        Output_File.write(str(dsc) + "\n")
        Output_File.write("The data sorted by Quick Sort is: " + "\n")
        Output_File.write(str(QuickSort(random, 0, len(random)-1)) + "\n")
        Output_File.write("The data sorted by Hybrid Sort with 50 threshold is: " + "\n")
        Output_File.write(str(HybridSort50(random, 0, len(random) - 1)) + "\n")
        Output_File.write("The data sorted by Hybrid Sort with 100 threshold is: " + "\n")
        Output_File.write(str(HybridSort100(random, 0, len(random) - 1)) + "\n")
        Output_File.write("The data sorted by Quick Sort with median of 3 as pivot: " + "\n")
        Output_File.write(str(quicksort(random, 0, len(random) - 1)) + "\n")

        head = None
        for key in random:
            head = LinkedList(key, head)
        head = linked_list_natural_merge_sort(head)[0]
        comparisons = linked_list_natural_merge_sort(head)[1]
        swaps = linked_list_natural_merge_sort(head)[2]
        Output_File.write("The data sorted by Natural Merge Sort with Linked List implementation: " + "\n")
        #Output_File.write(printList(head))
        Output_File.write(str(comparisons))
        Output_File.write(str(swaps))

    with open("ascending50.txt", mode="r") as AscendingOrder_File:
        asc = []
        for line in AscendingOrder_File.readlines():
            line.strip()
            asc.append(int(line.strip()))
        Output_File.write("The ascending ordered data is: " + "\n")
        Output_File.write(str(asc) + "\n")
        Output_File.write("The data sorted by Quick Sort is: " + "\n")
        Output_File.write(str(QuickSort(random, 0, len(random)-1)) + "\n")
        Output_File.write("The data sorted by Hybrid Sort with 50 threshold is: " + "\n")
        Output_File.write(str(HybridSort50(random, 0, len(random) - 1)) + "\n")
        Output_File.write("The data sorted by Hybrid Sort with 100 threshold is: " + "\n")
        Output_File.write(str(HybridSort100(random, 0, len(random) - 1)) + "\n")
        Output_File.write("The data sorted by Quick Sort with median of 3 as pivot: " + "\n")
        Output_File.write(str(quicksort(random, 0, len(random) - 1)) + "\n")

        head = None
        for key in random:
            head = LinkedList(key, head)
        head = linked_list_natural_merge_sort(head)[0]
        comparisons = linked_list_natural_merge_sort(head)[1]
        swaps = linked_list_natural_merge_sort(head)[2]
        Output_File.write("The data sorted by Natural Merge Sort with Linked List implementation: " + "\n")
        #Output_File.write(printList(head))
        Output_File.write(str(comparisons))
        Output_File.write(str(swaps))