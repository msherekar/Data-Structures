from msherekar_lab1.stack import Stack
from pathlib import Path


def convert(row):
    """
    This method converts a given prefix string into a postfix string using Stacks. It was made as a part of module
    based application for Lab-1 of Data Structures class. It takes in a prefix string, checks for its validity and
    gives out a postfix string. 03/02/2022
    :param row:
    :return:
    """

    stack_to_reverse = Stack()  # A stack to store the given string; also does the job of reversing to enable

    for character in row:  # reading from R>L

        if character == " ":
            print("Encountered a blank space in the prefix but it did not affect the conversion.")
            continue

        if character in ["!", "@", "#", "%", "^", "&", "(", ")"]:
            print("Encountered an invalid operator" + "(" + character + ")" +
                  " in the prefix but ignored it and finished the conversion.")
            continue

        if character in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            print("Encountered an integer" + "(" + character + ")" +
                  "in the prefix but ignored it and finished the conversion.")
            continue

        if character == "\n":
            # print("error")
            break
        if character == "\t":
            # print("error")
            break
        if character == "\r":
            print("error")
            break

        else:  # once errors have been taken care of push the remaining valid characters
            stack_to_reverse.push(character)

    # A set of valid operators to enable sorting of what goes into stack i.e alphabets into stack and operators not
    operators = ['$', '/', '*', '+', '-']
    stack = Stack()  # a stack to store the converted string

    while stack_to_reverse.is_notempty():
        try:
            i = stack_to_reverse.pop()
            if i not in operators:
                stack.push(i)
            else:
                a = stack.pop()
                b = stack.pop()
                postfix = a + b + i
                stack.push(postfix)
        except TypeError:
            continue

    converted_string = ""  # initiate an empty string to eventually to help write on a file

    while stack.is_notempty():  # a loop to add characters to string
        for i in stack.pop():
            converted_string = converted_string + i

    return converted_string




