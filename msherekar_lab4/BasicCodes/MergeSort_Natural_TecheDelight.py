# source:
# https://www.techiedelight.com/merge-sort-singly-linked-list/
from random import randint

# A Linked List Node
class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


# Function to print a given linked list
def printList(head):
    ptr = head
    while ptr:
        print(ptr.data, end=' —> ')
        ptr = ptr.next
    print('None')


# Takes two lists sorted in increasing order and merge their nodes
# to make one big sorted list, which is returned
def sortedMerge(a, b):
    # base cases
    if a is None:
        return b
    elif b is None:
        return a

    # pick either `a` or `b`, and recur
    if a.data <= b.data:
        result = a
        result.next = sortedMerge(a.next, b)

    else:
        result = b
        result.next = sortedMerge(a, b.next)

    return result


'''
	Split the given list's nodes into front and back halves,
	If the length is odd, the extra node should go in the front list.
	It uses the fast/slow pointer strategy
'''


def frontBackSplit(source):

    # if the length is less than 2, handle it separately
    if source is None or source.next is None:
        return source, None

    (slow, fast) = (source, source.next)

    # advance `fast` two nodes, and advance `slow` one node
    while fast:

        fast = fast.next
        if fast:
            slow = slow.next
            fast = fast.next

    # `slow` is before the midpoint of the list, so split it in two
    # at that point.
    ret = (source, slow.next)
    slow.next = None

    return ret


# Sort a given linked list using the merge sort algorithm
def mergesort(head):
    # base case — length 0 or 1
    if head is None or head.next is None:
        return head

    # split `head` into `a` and `b` sublists
    front, back = frontBackSplit(head)

    # recursively sort the sublists
    front = mergesort(front)
    back = mergesort(back)

    # answer = merge the two sorted lists
    return sortedMerge(front, back)


if __name__ == '__main__':

    Array_Length = 1000
    random_list = [randint(0, 10000) for i in range(Array_Length)]

    head = None
    for key in random_list:
        head = Node(key, head)

    # sort the list
    head = mergesort(head)

    # print the sorted list
    printList(head)
