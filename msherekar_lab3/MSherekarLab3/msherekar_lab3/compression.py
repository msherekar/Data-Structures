
def CalculateCompression(data, code):
    """
    This method calculates memory usage for given data and compressed data based on 8 bits and returns % compression.
    A handy program to show efficiency of huffman algorithm.
    :param data: given data
    :param code: calculated codes from huffman compression
    :return: total bits saved
    """

    before_compression = len(data) * 8
    after_compression = 0

    alphabets = code.keys()

    for alphabet in alphabets:
        count = data.count(alphabet)
        after_compression += count * len(code[alphabet])

    bits_saved = before_compression - after_compression
    percent_savings = (bits_saved / before_compression) * 100

    return percent_savings
