codes = dict()  # initialize a dictionary to store codes

def codify(node, val=''):
    """

    This method assigns huffman codes to each alphabet. It takes in a huffman tree as an input and return a dictionary
    of alphabets and their codes. The codes are in form of 0 & 1 (strings of bits). To give codes in form of 0s and 1s
    this method raverse the tree in pre-order fashion.

    :param node: huffman node
    :param val:
    :return: dictionary of nodes and their codes
    """

    newval = val + str(node.code)  # referring to the code

    if node.left:
        codify(node.left, newval)

    if node.right:
        codify(node.right, newval)

    if not node.left and not node.right:
        codes[node.alphabet] = newval

    return codes



