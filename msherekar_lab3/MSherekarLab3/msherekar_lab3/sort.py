from msherekar_lab3.heap import MinHeap
from msherekar_lab3.node import Node
from msherekar_lab3.code import codify


def heapsort(node_heap):
    """
    This method sorts a heap of nodes (with data as alphabets and their frequency) in ascending order following nlogn(?)
    Then, while sorting is going on, two smallest nodes are removed and added to a new heap. It takes in a heap of nodes
    as in input and gives out a huffman tree. It is a tree with master node and all its leafs being alphabets.
    This huffman tree is traversed to come up with codes for each alphabet.

    :param heap_node: a heap of nodes of alphabets and frequencies
    :return: huffman tree
    """

    # Create an instance of class MinHeap to store the sorted heap of nodes
    sorted_nodeheap = MinHeap()

    # Again following piece of code is extremely powerful. It iterates over node_heap(input); in doing so it 1) finds
    # minimum root of node_heap and inserts into a new heap called sorted_heap (of same nodes). In doing so, nodes are
    # being moved from one heap to another and both maintain their heap property
    while node_heap.currentsize > 0:
        sorted_nodeheap.insert(node_heap.minroot())

    # following piece of code removes, at a time, two minimum nodes out of sorted heaps and adds them up. Then, the
    # complex node is inserted back into the sorted heap. In doing so, the complex node has two new children i.e
    # the two removed nodes.
    while sorted_nodeheap.currentsize > 1:
        left_child = sorted_nodeheap.minroot()  # smallest root
        right_child = sorted_nodeheap.minroot()  # 2nd smallest

        left_child.code = 0  # setting up the codes which will eventually compress because its just 0 and 1
        right_child.code = 1

        new_node_freq = left_child.freq + right_child.freq
        new_node_alphabets = left_child.alphabet + right_child.alphabet

        new_node = Node(new_node_alphabets, new_node_freq, left_child, right_child)

        sorted_nodeheap.insert(new_node)

    return sorted_nodeheap
