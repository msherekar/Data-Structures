from msherekar_lab3.convert import convert
from msherekar_lab3.sort import heapsort
from msherekar_lab3.code import codify
from msherekar_lab3.huffman_compress import compress
from msherekar_lab3.huffman_decompress import decompress
from heap import MinHeap
import re
from node import Node

with open('out.txt', mode="w", encoding="utf-8") as output_file:
    with open('FreqTable.txt', mode="r", encoding="utf-8") as file:
        node_heap = MinHeap()

        for line in file:
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

    output_file.write("The compressed lines are:" + "\n")
    with open('ClearText.txt', mode="r", encoding="utf-8") as file:
        for line in file:
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

    print("\n")
    output_file.write("The decompressed lines are:" + "\n")
    with open('Encoded.txt', mode="r", encoding="utf-8") as file:
        for line in file:
            try:
                print(decompress(line, huff_node))

                output_file.write(decompress(line, huff_node))
                output_file.write("\n")

            except KeyError:
                print("unknown character encountered")

for key, value in huff_codes.items():

    print(key, "->", value)

