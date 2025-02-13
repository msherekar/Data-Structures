from msherekar_lab3.node import Node

def convert(line):
    """
    Convert each line of frequency file into a node. Splits Alphabet:Frequency into a list of two elements and
    creates a node instance using Node class. Each node created will have two pices of information (alphabet and frequency)
    Also, secondary information like children nodes and values for branches can be added.

    :return: a instance of Node class with two pieces of data from frequency table in the text file
    """
    line_list = line.rstrip('\n').split()

    line_list[2] = int(line_list[2])

    node = Node(line_list[0], line_list[2])

    return node










