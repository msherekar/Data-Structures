# This is an implementation of Natural Merge Sort using a Linked List
# Source: https://codereview.stackexchange.com/questions/211149/linked-list-natural-merge-sort-in-python

from random import randint

# A Linked List Node
class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


# Linked list is either empty or a value and a link to the next list
empty = None  # empty list


class LinkedList(object):
    __slots__ = "value", "next"

    def __init__(self, value, next=empty):
        self.value = value
        self.next = next

    def __le__(self, other):
        return self.value <= other.value

    def __lt__(self, other):
        return self.value < other.value


def reverse(head, size=-1):
    """
    reference: https://stackoverflow.com/a/22049871/3552
    """
    new_head = None
    while head:
        temp = head
        head = temp.next
        temp.next = new_head
        new_head = temp

        size -= 1
        if not size:
            tail = new_head
            while tail.next:
                tail = tail.next
            tail.next = head
            return new_head

    return new_head


def find_next_stop(head):
    if head is empty:
        return head, 0, empty
    next_node = head.next
    if next_node is empty:
        return head, 1, empty

    size = 2

    if head <= next_node:
        while next_node.next and next_node <= next_node.next:
            size += 1
            next_node = next_node.next
        next_node = next_node.next
    else:
        while next_node.next and next_node.next < next_node:
            size += 1
            next_node = next_node.next
        next_node = next_node.next
        head = reverse(head, size)

    return head, size, next_node


def linked_list_natural_merge_sort(head):
    p = q = head
    psize = 0
    tail = empty

    while q is not empty:
        tail = empty
        q, qsize, next_q = find_next_stop(q)
        msize = psize + qsize

        while qsize > 0 or psize > 0:
            if psize == 0:
                e, q = q, q.next
                qsize -= 1
            elif qsize == 0:
                e, p = p, p.next
                psize -= 1
            elif p <= q:
                e, p = p, p.next
                psize -= 1
            else:
                e, q = q, q.next
                qsize -= 1

            if tail is empty:
                head = e
            else:
                tail.next = e
            tail = e

        psize = msize
        q = next_q
        p = head

    if tail is not empty:
        tail.next = empty

    return head


def mklist(initializer):
    it = reversed(initializer)
    try:
        x = next(it)
    except StopIteration:
        return empty
    else:
        head = LinkedList(x)
        for value in it:
            head = LinkedList(value, head)
        return head


def walk(head, size=-1):
    while head is not empty:
        if size:
            size -= 1
        else:
            break
        yield head.value
        head = head.next


def tolist(head, size=-1):
    return list(walk(head, size))

# Function to print a given linked list
def printList(head):
    ptr = head
    while ptr:
        print(ptr.value, end=' —> ')
        ptr = ptr.next
    print('None')


if __name__ == '__main__':

    Array_Length = 100
    random_list = [randint(0, 10000) for i in range(Array_Length)]

    head = None
    for key in random_list:
        head = LinkedList(key, head)

    # sort the list
    head = linked_list_natural_merge_sort(head)

    # print the sorted list
    printList(head)
