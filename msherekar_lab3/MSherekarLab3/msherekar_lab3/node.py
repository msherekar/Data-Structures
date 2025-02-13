"""
This class (data structure) is to store data in a memory location(?) and then point to (connect to) two other nodes
(memory locations). Also, branch from node to its children can be labelled (self.code), It can be used for binary trees,
Linkedlists and other data structures. Very handy !

Specifically, this node class has two properties (priority queue application as well) - alphabet and its frequency.
"""


class Node:
    def __init__(self, alphabet, freq, left=None, right=None):
        # frequency of alphabet
        self.freq = freq

        # name of alphabet
        self.alphabet = alphabet

        # left child of the node
        self.left = left

        # right child of the node
        self.right = right

        # code for the path i.e 0 for left and 1 for right
        self.code = ''

    # to print node
    def __repr__(self) -> str:
        return f" {self.alphabet, self.freq}, {self.left}, {self.right}"
