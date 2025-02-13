# Used the given main file in proj0 and modified for my module.
# This file is the entry point into this program when the module is executed
# as a standalone program. IE 'python -m msherekar_lab3'. This file is NOT run during
# imports. This whole file is basically the java equivalent of:
# public static void main(string args[]), or c's int main();

# Generally used to process command line arguments and 'launch' the program
from pathlib import Path
import argparse

from msherekar_lab3 import process_files

# Argument parser is an amazing tool. It's worth mastering
arg_parser = argparse.ArgumentParser()
arg_parser.add_argument("frequency_file", type=str, help="Input File Pathname")
arg_parser.add_argument("input_file_to_compress", type=str, help="Input File to encode")
arg_parser.add_argument("input_file_to_decompress", type=str, help="Input File to decode")
arg_parser.add_argument("output_file", type=str, help="Output File Pathname")
args = arg_parser.parse_args()

# pathlib.Path is also a fantastic built in tool and has a lot of great
# features. Please look it up! I promise it's worth it.
in_path1 = Path(args.frequency_file)
in_path2 = Path(args.input_file_to_compress)
in_path3 = Path(args.input_file_to_decompress)
out_path = Path(args.output_file)

with in_path1.open('r') as frequency_file, in_path2.open('r') as input_file_to_compress, in_path3.open('r') \
        as input_file_to_decompress, out_path.open('w') as output_file:

    process_files(frequency_file, input_file_to_compress, input_file_to_decompress, output_file)

