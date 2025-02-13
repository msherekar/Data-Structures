from typing import TextIO
from msherekar_lab3.convert import convert
from msherekar_lab3.sort import heapsort
from msherekar_lab3.code import codify
from msherekar_lab3.huffman_compress import compress
from msherekar_lab3.huffman_decompress import decompress
from msherekar_lab3.heap import MinHeap
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
    # global huff_codes, huff_tree
    node_heap = MinHeap()
    for line in frequency_file.readlines():
        converted_line = convert(line)
        node_heap.insert(converted_line)

    print("The initial heap is: ")
    print(node_heap, '\n')
    output_file.write("The initial heap is: " + "\n" + str(node_heap) + "\n")
    output_file.write("\n")

    huff_tree = heapsort(node_heap)
    print("Sorted node heap i.e hufftree is: " + "\n " + str(huff_tree))
    output_file.write("Sorted node heap i.e hufftree is: " + "\n " + str(huff_tree) + "\n")
    output_file.write("\n")

    huff_node = huff_tree.minroot()
    print("The root node of sorted node heap is: " + "\n" + str(huff_node) + "\n")
    output_file.write("The root node of sorted node heap is: " + "\n" + str(huff_node) + "\n")
    output_file.write("\n")

    huff_codes = codify(huff_node)
    print("The huff codes for given frequency table are: " + "\n" + str(huff_codes) + "\n")
    output_file.write("The huff codes for given frequency table are: " + "\n" + str(huff_codes) + "\n")
    output_file.write("\n")

    output_file.write("\n")
    output_file.write("The compressed lines are:" + "\n")

    for line in input_file_to_compress.readlines():
        # getting rid of punctuations, spaces and making everything upper case
        line = re.sub(r'[^\w\s]', '', line)
        line = line.replace(" ", "")
        line = line.upper().strip()
        try:
            print(compress(line, huff_codes), '\n')

            output_file.write(compress(line, huff_codes))
            output_file.write("\n")

        except KeyError:
            print("unknown character encountered")

    output_file.write("\n")
    output_file.write("The decompressed lines are:" + "\n")

    for line in input_file_to_decompress.readlines():
        try:
            print(decompress(line, huff_node))
            output_file.write(decompress(line, huff_node))
            output_file.write("\n")

        except KeyError:
            print("unknown character encountered")
