from typing import TextIO
from msherekar_lab2.convert import convert


def process_files(input_file: TextIO, output_file: TextIO) -> None:
    """
    This method was made for Lab-2 (using Lab-1) of Data Structures class. It accepts name of input and outfile file and
    then gives out a output file. The function of this method is to convert pre-fix strings in the given text file into
    post-fix strings via command line arguments. It uses convert method from another file and TextIO module. 03/26/2022

    :param input_file:
    :param output_file:
    :return:
    """
    for line in input_file.readlines():
        try:
            print(convert(line))
            output_file.write(convert(line))
            output_file.write("\n")
        except IndexError:
            print("Given prefix cannot be converted into post fix")
            output_file.write("Given prefix cannot be converted into post fix")
            output_file.write("\n")
        except TypeError:
            print("None was returned")