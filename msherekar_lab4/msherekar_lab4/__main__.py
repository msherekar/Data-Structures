import argparse
from pathlib import Path
import os
from glob import glob
from msherekar_lab4 import process_files

# Write basic steps to create and parse an argument using argparse
arg_parser = argparse.ArgumentParser()

arg_parser.add_argument("folder", type=Path, help="path to your input folder")

args = arg_parser.parse_args()

in_path = Path(args.folder)
out_path = Path(in_path, "out")

# Select file in given folder and use its name to create a new outfile file
# Very important step, wasted lots of time here
for file in in_path.glob("*.txt"):
    output1 = file.with_suffix(".qs_normal")
    output2 = file.with_suffix(".qs_hybrid50")
    output3 = file.with_suffix(".qs_hybrid100")
    output4 = file.with_suffix(".qs_med3")
    output5 = file.with_suffix(".ms_nat_ll")

    with open(file, "r") as infile, \
            open(output1, "w") as outfile1, \
            open(output2, "w") as outfile2, \
            open(output3, "w") as outfile3, \
            open(output4, "w") as outfile4, \
            open(output5, "w") as outfile5:

        process_files(infile, outfile1, outfile2, outfile3, outfile4, outfile5)
