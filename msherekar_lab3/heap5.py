"""
This class creates a Heap (type of Binary Tree). Specifically, this class creates a minimum heap. Property of a minimum
heap is that parent node is always smaller than its children nodes. This particular class of heap makes sure that the
parent node is smaller in terms of frequency of alphabet, type of alphabet and length of alphabets.

This heap class is made for nodes that have two properties (or data) stored in them - alphabets and their frequencies.
It was created for Lab-3 (Huffman compression & decompression) of Data Structures class EN.605.202
"""


class MinHeap:

    def __init__(self):

        # first element is better be zero for convenience of defining parent & children nodes in terms of (i)

        self.heaplist = [0]  # list/array implementation
        self.currentsize = 0

    def swapup(self, i):  # method to move a node up if it is smaller than its parent

        while i // 2 > 0:

            # comparing frequencies of child (i) and parent (i//2)

            if self.heaplist[i].freq < self.heaplist[i // 2].freq:
                self.heaplist[i // 2], self.heaplist[i] = self.heaplist[i], self.heaplist[i // 2]

            i = i // 2

    def insert(self, j):  # method to insert a new node to heap i.e list and swap up if needed

        self.heaplist.append(j)

        self.currentsize = self.currentsize + 1

        self.swapup(self.currentsize)

    def minchild(self, i):  # To find index of smaller child based on frequency and then on alphabet type & size

        if i * 2 + 1 > self.currentsize:
            return i * 2

        # if alphabets are equal, then comparing frequencies
        if self.heaplist[i * 2].alphabet == self.heaplist[i * 2 + 1].alphabet:
            # simple comparison of frequencies
            if self.heaplist[i * 2].freq < self.heaplist[i * 2 + 1].freq:
                return i * 2

            else:
                return i * 2 + 1

        else: # making decisions by alphabets only


            # if single alphabets then checking their ord values
            if len(self.heaplist[(2 * i) + 1].alphabet) == 1 and self.heaplist[(2 * i)].alphabet == 1:

                if ord(self.heaplist[(2 * i) + 1].alphabet) < ord(self.heaplist[(2 * i)].alphabet):
                    return i * 2 + 1

                else:
                    return i * 2

            # comparing lengths to decide which child is smaller
            elif len(self.heaplist[(2 * i) + 1].alphabet) < len(self.heaplist[(2 * i)].alphabet):
                return 2 * i + 1

            elif len(self.heaplist[(2 * i) + 1].alphabet) > len(self.heaplist[(2 * i)].alphabet):
                return 2 * i

            else:
                # comparing complexity of multi-alphabet strings
                if min(self.heaplist[2 * i].alphabet, self.heaplist[2 * i + 1].alphabet) == self.heaplist[2 * i].alphabet:
                    return 2 * i

                else:
                    return 2 * i + 1



    def swapdown(self, i):  # to move a newly added node on top of heap to its appropriate location

        while (i * 2) <= self.currentsize:

            mc = self.minchild(i)   # mc is index of smaller child

            if self.heaplist[i].freq > self.heaplist[mc].freq:
                self.heaplist[i], self.heaplist[mc] = self.heaplist[mc], self.heaplist[i]

            i = mc

    def minroot(self):  # important method to retrieve root i.e top node of the heap

        minval = self.heaplist[1] # store top node i.e root into a variable so that last node could be substituted

        self.heaplist[1] = self.heaplist[self.currentsize] # moving the last node onto to top

        self.currentsize = self.currentsize - 1 # reduce the size of heap

        self.heaplist.pop() # remove the top node array location (?)

        self.swapdown(1) # put the newly added node to its appropriate location

        return minval

    def minheapify(self, nodelist): # a method to make sure heap follows its basic property i.e parent < children

        i = len(nodelist) // 2

        self.currentsize = len(nodelist)

        self.heaplist = [0] + nodelist[:]

        while i > 0:
            self.swapdown(i)
            i = i - 1

    def __repr__(self) -> str:
        return f" {self.heaplist}"
