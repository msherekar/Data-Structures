def decompress(compressedString, treeRoot):

    node = treeRoot
    result = ""

    for bit in compressedString:

        # Go to left or right child based on bit value
        if bit == '0':
            node = node.left

        else:
            node = node.right

        # If the node is a leaf, add the character to the
        # decompressed result and go back to the root node

        if node.left == None and node.right == None:
            result += node.alphabet
            node = treeRoot

    return result


