from sys import stderr
from typing import TextIO
from msherekar_lab1.convert import convert

def process_files(input_file: TextIO, output_file: TextIO) -> None:
    """
    This method was made for Lab-1 of Data Structures class. It accepts name of input and outfile file and then gives
    out a output file. The function of this method is to convert pre-fix strings into post-fix strings via command line
    arguments. It uses convert method from another file and TextIO module. 03/02/2022

    :param input_file:
    :param output_file:
    :return:
    """
    next_line = input_file.readline()                               # initiate the loop

    while next_line is not None and next_line != " ":                # loop to iterate all line in text file
        try:
            postfix = convert(next_line)                            # usage of convert module

        finally:
            next_line = input_file.readline()

        output_file.write(postfix)                                  # print the converted string into a text file
        output_file.write('\n')











