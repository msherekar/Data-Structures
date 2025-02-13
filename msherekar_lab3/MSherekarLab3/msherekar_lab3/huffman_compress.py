def compress(line, code):
    """

    This method converts a english sentence into a Huffman code. It requires a set of alphabets and derived huffman
    code to compress.

    :param line: any english sentence or alphabets
    :param code: derived huffman code from frequency data
    :return: compressed sentence in form of 0s and 1s

    """

    compressed_sentence = []

    for c in line:
        compressed_sentence.append(code[c])

    string = ''.join([str(item) for item in compressed_sentence])

    return string


