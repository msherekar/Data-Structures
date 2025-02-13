# Used the given main file in proj0 and modified for my module.
# This file is the entry point into this program when the module is executed
# as a standalone program. IE 'python -m msherekar_lab3'. This file is NOT run during
# imports. This whole file is basically the java equivalent of:
# public static void main(string args[]), or c's int main();

# Generally used to process command line arguments and 'launch' the program
from pathlib import Path
import argparse
from msherekar_lab4 import process_files

# Argument parser is an amazing tool. It's worth mastering
arg_parser = argparse.ArgumentParser()
arg_parser.add_argument("AscendingOrderFile", type=str, help="File with ascending ordered data")
arg_parser.add_argument("DescendingOrderFile", type=str, help="File with descending ordered data")
arg_parser.add_argument("RandomOrderFile", type=str, help="File with random ordered data")
#arg_parser.add_argument("output_file", type=str, help="Output File Pathname")
args = arg_parser.parse_args()

# pathlib.Path is also a fantastic built in tool and has a lot of great
# features. Please look it up! I promise it's worth it.
in_path1 = Path(args.AscendingOrderFile)
in_path2 = Path(args.DescendingOrderFile)
in_path3 = Path(args.RandomOrderFile)
#out_path = Path(args.output_file)

with in_path1.open('r') as AscendingOrderFile, in_path2.open('r') as DescendingOrderFile, in_path3.open('r') \
        as RandomOrderFile:

    process_files(AscendingOrderFile, DescendingOrderFile, RandomOrderFile)


#####
import argparse
from pathlib import Path
import os
from msherekar_lab4 import process_folders

arg_parser = argparse.ArgumentParser()

arg_parser.add_argument("--input_dir", type=Path, default=Path(__file__).absolute().parent / "data",
                        help="path to your subdirectory", required=True)

arg_parser.add_argument("--output_dir", type=Path, default=Path(__file__).absolute().parent / "data",
                        help="path to your subdirectory", required=True)

args = arg_parser.parse_args()

# represents path of input folder
in_path = Path(args.input_dir)
out_path = Path(args.output_dir)

with in_path as InFolder, out_path as OutFolder:
    process_folders(InFolder, OutFolder)

#########
def process_file(filename):
    data = []
    with open(filename, mode='r') as datafile:
        for line in datafile.readlines():
            data.append(int(line.strip()))
    QuickSort(data, 0, len(data) - 1)
    with open("out.txt", mode='a') as Output_File:
        Output_File.write("The random ordered data is: " + "\n")
        Output_File.write(str(data) + "\n")
        Output_File.write("The data sorted by Quick Sort is: " + "\n")
        Output_File.write(str(QuickSort(data, 0, len(data) - 1)) + "\n")
    return
######
import argparse
from pathlib import Path
from msherekar_lab4 import process_folders
arg_parser = argparse.ArgumentParser()
arg_parser.add_argument("--inputdir", help="path to your subdirectory", required=True)
arg_parser.add_argument("--outputdir", help="path to your subdirectory", required=True)
args = arg_parser.parse_args()


in_path = Path(args.inputdir)
out_path = Path(args.outputdir)

with in_path as InFolder, out_path as OutFolder:
    process_folders(InFolder, OutFolder)
######
from typing import TextIO
import sys
import os
from QuickSort_Counts import QuickSort


def process_folders(InFolder, OutFolder):
    for dirpath, dirnames, files in os.walk(InFolder):
        for file_name in files:
            process_file(file_name)

            # use outfolder as destination of output files
            write_results(listname, OutFolder)

        def process_file(filename):
            data = []
            with open(filename, mode='r') as datafile:
                for line in datafile.readlines():
                    data.append(int(line.strip()))
            QuickSort(data, 0, len(data) - 1)
            return data

        def write_results(listname: TextIO, foldername: TextIO) -> None:
            """
            :param foldername:
            :param listname: name of list given out by process files; contains sorted list
            :return:
            """
            # need to make sure each file gets a special name after the sort
            with open("out.txt", mode="a") as Output_File:
                Output_File.write("The data sorted by Quick Sort is: " + "\n")
                Output_File.write(str(listname) + "\n")
            return
    return



###########################################################
from typing import TextIO
def process_files(RandomOrder_File: TextIO, DescendingOrder_File: TextIO, AscendingOrder_File: TextIO,
                  Output_File: TextIO) -> None:
    # reading random order data into a list
    random = []
    for line in RandomOrder_File.readlines():
        line.strip()
        random.append(int(line.strip()))
        Output_File.write("The random ordered data is: ")
        Output_File.write(str(random))
        Output_File.write("\n")

    dsc = []
    for line in DescendingOrder_File.readlines():
        line.strip()
        dsc.append(int(line.strip()))
        Output_File.write("The descending ordered data is: ")
        Output_File.write(str(dsc))
        Output_File.write("\n")

    asc = []
    for line in AscendingOrder_File.readlines():
        line.strip()
        asc.append(int(line.strip()))
        Output_File.write("The ascending ordered data is: ")
        Output_File.write(str(asc))
        Output_File.write("\n")
########

# Used the given main file in proj0 and modified for my module.
# This file is the entry point into this program when the module is executed
# as a standalone program. IE 'python -m msherekar_lab4'. This file is NOT run during
# imports. This whole file is basically the java equivalent of:
# public static void main(string args[]), or c's int main();

# Generally used to process command line arguments and 'launch' the program
from pathlib import Path
import argparse

from msherekar_lab3 import process_files

# Argument parser is an amazing tool. It's worth mastering

arg_parser = argparse.ArgumentParser()
arg_parser.add_argument("RandomOrder_File", type=str, help="Input File to decode")
arg_parser.add_argument("DescendingOrder_File", type=str, help="Input File with data in descending order")
arg_parser.add_argument("AscendingOrder_File", type=str, help="Input File with data in ascending order")
arg_parser.add_argument("Output_File", type=str, help="Output File Pathname")
args = arg_parser.parse_args()

# pathlib.Path is also a fantastic built in tool and has a lot of great
# features. Please look it up! I promise it's worth it.
in_path1 = Path(args.RandomOrder_File)
in_path2 = Path(args.DescendingOrder_File)
in_path3 = Path(args.AscendingOrder_File)
out_path = Path(args.Output_File)

with in_path1.open('r') as RandomOrder_File, in_path2.open('r') as DescendingOrder_File, in_path3.open('r') \
        as AscendingOrder_File, out_path.open('a') as Output_File:

    process_files(RandomOrder_File, DescendingOrder_File, AscendingOrder_File, Output_File)

#####
