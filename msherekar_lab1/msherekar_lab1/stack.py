"""
This file consists of code to make a stack class. It has basic stack methods like push, pop etc. This is a list application
of stack data structure. 03/02/2022
"""
# writing a stack class
class Stack:
    def __init__(self):
        self.items = []

    def push(self, data):
        self.items.append(data)

    def size(self):
        return len(self.items)

    def is_empty(self):
        return True if self.size() == 0 else False

    def is_notempty(self):
        return True if self.size() != 0 else False

    def pop(self):
        if self.items:
            return self.items.pop()
        else:
            return None  # This is error handling for empty list

    def peek(self):
        return self.items[0]

    def print(self):
        return self.items[::-1]  # change to return in reverse later
