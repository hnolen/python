#! /usr/bin/env python3

# Usage: ./move_reads.py --reads <path to directory containing read folders> --new <path t$

# This script will move reads from subdirectories into one directory.
# You should create the destination directory prior to running this code.

# Import required modules
import argparse
import os
import shutil

# Establish command line arguments
parser = argparse.ArgumentParser()
parser.add_argument('--reads', type=str, help='path to directory containing folders with reads')
parser.add_argument('--new', type=str, help="new directory to copy reads into")
args=parser.parse_args()

# Scan through each subdirectory and move contents to destination directory if they are .gz files
counter = 0
for root, subdirs, files in os.walk(args.reads):
    for file in files:
        if file.endswith("gz"):
            path = os.path.join(root, file)
            dest = os.path.join(args.new, file)
            shutil.copy(path, dest)
            counter += 1

print("{0} reads were copied to {1}".format(counter, args.new))


