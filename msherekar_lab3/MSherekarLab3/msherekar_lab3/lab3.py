from typing import TextIO
from msherekar_lab3.convert import convert
from msherekar_lab3.sort import heapsort
from msherekar_lab3.code import codify
from msherekar_lab3.huffman_compress import compress
from msherekar_lab3.huffman_decompress import decompress
from msherekar_lab3.heap import MinHeap
from msherekar_lab3.compression import CalculateCompression
import re
import textwrap


def process_files(frequency_file: TextIO, input_file_to_compress: TextIO, input_file_to_decompress: TextIO,
                  output_file: TextIO) -> None:
    """
    :param input_file_to_compress:
    :param input_file_to_decompress:
    :param frequency_file:
    :param output_file:
    :return:
    """
    # firstly, obtaining codes from frequency data
    # and adding them to a heap data structure

    node_heap = MinHeap()

    for line in frequency_file.readlines():
        converted_line = convert(line)
        node_heap.insert(converted_line)

    # sort the tree to be able to extract huffman root
    huff_tree = heapsort(node_heap)
    huff_node = huff_tree.minroot()

    output_file.write("The huffman tree in pre-order is: " + "\n" + textwrap.fill(str(huff_node), width=80) + "\n")
    output_file.write("\n")

    # use the huffman tree to assign codes to each alphabet
    huff_codes = codify(huff_node)
    output_file.write("The huff codes for given frequency table are: " + "\n" + textwrap.fill(str(huff_codes), width=80) + "\n")
    output_file.write("\n")

    # compression in action
    output_file.write("The compressed version of given data is:" + "\n")

    for line in input_file_to_compress.readlines():
        # getting rid of punctuations, spaces and making everything upper case
        line = re.sub(r'[^\w\s]', '', line)
        line = line.replace(" ", "")
        line = line.upper().strip()
        try:
            output_file.write(textwrap.fill(compress(line, huff_codes), width=80))
            output_file.write("\n")
            y = CalculateCompression(line, huff_codes)
            output_file.write(str(round(y, 2)) + "%" + " " + "data compression achieved" + "\n")
            output_file.write("\n")

        except KeyError:
            print("unknown character encountered")

    # decoding in action
    output_file.write("\n")
    output_file.write("The decompressed version of given data is :" + "\n")

    for line in input_file_to_decompress.readlines():
        try:
            output_file.write(decompress(line, huff_node))
            output_file.write("\n")

        except KeyError:
            print("unknown character encountered")
